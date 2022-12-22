#REFATORANDO O CODIGO DO DIA 07

import requests
import json
##import pprint

# r=requests.get('https://www.google.com')
# print(r.status_code)  #resposta 20 indica que a requisição foi bem sucedida.

#print(r.headers)
#print(r.headers['Date'])
#print(r.text) #essa e a resposta HTML que irá gerar a página do google

#iremos criar um programa que irá utilizar uma API para previsão do tempo chamada accuweather, https://developer.accuweather.com/
#porém, este programa ja precisa de latitude e longitude, então iremos obter a localização do usuário que esta utilizando
# o programa com outra API chamada geo plugin

accuweather_apikey= '50GSIFXKnwmcNgXw2F2fhlvKX8j0xFdU'

def pegarCoordendas():
    r=requests.get('http://www.geoplugin.net/json.gp')

    if r.status_code != 200 :
        print("Não foi possível encontrar a localização!")
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
        print("Não foi possível encontrar a codnição do tempo!")
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
##Inicio do programa:

coordenadas= pegarCoordendas()
try:
    local=pegarCodigoLocal(coordenadas['lat'], coordenadas['long'])
    climaAtual= pegarTempoAgora(local['codigoLocal'], local['nomeLocal'])

    print('Clima atual em '+climaAtual['nomeLocal']+' é:')
    print(climaAtual['textoClima'])
    print('Temperatura: '+str(climaAtual['temperatura'])+"\xb0"+"C")
except:
    print("N]ao foi possível obter o clima!")
