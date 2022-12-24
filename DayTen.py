
import requests
import json
from datetime import date


accuweather_apikey= '50GSIFXKnwmcNgXw2F2fhlvKX8j0xFdU'
diasSemana=['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira' 
, 'Sexta-feira', 'Sábado', 'Domingo']

def pegarCoordendas():
    r=requests.get('http://www.geoplugin.net/json.gp')

    if r.status_code != 200 :
        print("Não foi possível encontrar a localização")
        return None
    else: 
        try:
            localizacao= json.loads(r.text) #irá transformar o arquivo em um dicionario para trabalharmos com as chaves
            #print(pprint.pprint(localizacao)) #importei o modulo pprint para organizar o dicionario pulando linha
            coordenadas={}
            coordenadas['lat']= localizacao['geoplugin_latitude']
            coordenadas['long']= localizacao['geoplugin_longitude'] #criar uma chave pro dicionario chada long e outra lat
            return coordenadas
        except: 
            return None

#O proximo passo é utilizar a API para conseguir a previsao do tempo da latitude e longitude anterior
# A \ pula linha e o '+' quer dizer que e continuação da linha anterior

def pegarCodigoLocal(lat, long):
    locationAPI_url="http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
    + "search?apikey=" + accuweather_apikey \
        +"&q=" + lat + "%2C%20"+ long + "&language=pt-br"


    r =requests.get(locationAPI_url)

    if (r.status_code != 200) :
        print("Não foi possível encontraro codigo do local!")
        return None
    else: 
        try:
            print("Localização encontrada!")
            locationResponse=json.loads(r.text)
            infoLocal={}
            #print( pprint.pprint(locationResponse))
            infoLocal['nomeLocal']= locationResponse['LocalizedName']+', '\
                + locationResponse['AdministrativeArea']['LocalizedName']+ ', '\
                +locationResponse['Country']['LocalizedName']+ '. '
            infoLocal['codigoLocal']=locationResponse['Key']
            return infoLocal
        except: 
            return None

    print('_______________________________')

def pegarTempoAgora(codigoLocal, nomeLocal):     
    currentConditionsAPIUrl="http://dataservice.accuweather.com/currentconditions/v1/" \
    +codigoLocal+"?apikey="+ accuweather_apikey+"&language=pt-br"

    r =requests.get(currentConditionsAPIUrl)

    if (r.status_code != 200) :
        print("Não foi possível encontrar a condição do tempo!")
        return None
    else: 
        try:
            print("Condições encontradas!")
            currentResponse=json.loads(r.text)
            #print( pprint.pprint(currentResponse))
            infoClima={}
            infoClima['textoClima']= currentResponse[0]['WeatherText']
            infoClima['temperatura']= currentResponse[0]['Temperature']['Metric']['Value']
            infoClima['nomeLocal']= nomeLocal
            return infoClima
        except:
            return None

def verificaTempo5Days(codigoLocal):
    r=requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/5day/" +codigoLocal \
    +"?apikey="+ accuweather_apikey+"&language=pt-br&metric=true")

    if r.status_code != 200 :
        print("Não foi possível encontrar as condições!")
        return None
    else: 
        try:
            dias= json.loads(r.text) 
            tempo5Dias=[]
    
            for dia in dias['DailyForecasts']:
                climaDia={}
                climaDia['max']= dia['Temperature']['Maximum']['Value']
                climaDia['min']= dia['Temperature']['Minimum']['Value']
                climaDia['clima']=dia['Day']['IconPhrase']
                diasDaSemana=int(date.fromtimestamp(dia['EpochDate']).strftime("%w"))
                climaDia['dia']= diasSemana[diasDaSemana]
                tempo5Dias.append(climaDia)
            return tempo5Dias
        except: 
            return None


##Inicio do programa:

coordenadas= pegarCoordendas()
try:
    local=pegarCodigoLocal(coordenadas['lat'], coordenadas['long'])
    climaAtual= pegarTempoAgora(local['codigoLocal'], local['nomeLocal'])
    previsoes=verificaTempo5Days(local['codigoLocal'])
    print('Clima atual em '+climaAtual['nomeLocal']+' é:')
    print(climaAtual['textoClima'])
    print('Temperatura: '+str(climaAtual['temperatura'])+"\xb0"+"C")
    print('\n Clima para hoje e para os próximos 5 dias: \n')
    
    for dia in previsoes:
        print(dia['dia'])
        print('Minima: '+str(dia['min']))
        print('Maxima: '+str(dia['max']))
        print('Clima: '+dia['clima'])
except:     
    print("Nao foi possível obter o clima!")
