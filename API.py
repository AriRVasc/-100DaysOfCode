import requests
import json
import pprint

r=requests.get('https://www.google.com')
print(r.status_code)  #resposta 20 indica que a requisição foi bem sucedida.

#print(r.headers)
#print(r.headers['Date'])
#print(r.text) #essa e a resposta HTML que irá gerar a página do google

#iremos criar um programa que irá utilizar uma API para previsão do tempo chamada accuweather, https://developer.accuweather.com/
#porém, este programa ja precisa de latitude e longitude, então iremos obter a localização do usuário que esta utilizando
# o programa com outra API chamada geo plugin

accuweather_apikey= '50GSIFXKnwmcNgXw2F2fhlvKX8j0xFdU'
loc=requests.get('http://www.geoplugin.net/json.gp')

if loc.status_code != 200 :
    print("Não foi possível encontrar a localização!")
else: 
    localizacao= json.loads(loc.text) #irá transformar o arquivo em um dicionario para trabalharmos com as chaves
    #print(pprint.pprint(localizacao)) #importei o modulo pprint para organizar o dicionario pulando linha
    long= localizacao['geoplugin_longitude']
    lat= localizacao['geoplugin_latitude']
    print(long)
    print(lat)

#O proximo passo é utilizar a API para conseguir a previsao do tempo da latitude e longitude anterior
# A \ pula linha e o '+' quer dizer que e continuação da linha anterior
locationAPI_url="http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
+ "search?apikey=" + accuweather_apikey \
    +"&q=" + lat + "%2C%20"+ long + "&language=pt-br"


r2 =requests.get(locationAPI_url)

if (r2.status_code != 200) :
    print("Não foi possível encontrar a localização!")

else: 
    print("Localização encontrada!")
    locationResponse=json.loads(r2.text)
    #print( pprint.pprint(locationResponse))
    nomeLocal= locationResponse['LocalizedName']+', '\
        + locationResponse['AdministrativeArea']['LocalizedName']+ ', '\
        +locationResponse['Country']['LocalizedName']+ '. '
    codigoLocal=locationResponse['Key']

    print("Local: ", nomeLocal)
    print("Código do Local: ", codigoLocal)

print('_______________________________')

        
currentConditionsAPIUrl="http://dataservice.accuweather.com/currentconditions/v1/" \
+codigoLocal+"?apikey="+ accuweather_apikey+"&language=pt-br"

r3 =requests.get(currentConditionsAPIUrl)

if (r3.status_code != 200) :
    print("Não foi possível encontrar a codnição do tempo!")

else: 
    print("Condições encontradas!")
    currentResponse=json.loads(r3.text)
    #print( pprint.pprint(currentResponse))
    textoClima= currentResponse[0]['WeatherText']
    temperatura= currentResponse[0]['Temperature']['Metric']['Value']
       

    print("O clima é:  ", textoClima)
    print("A temperatura é: ", str(temperatura)+"° C")