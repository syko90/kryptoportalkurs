from django.shortcuts import render
import requests
import json
from . import jprint
from web3 import Web3


# Create your views here.
def portfel(request):
    infura_url = "https://mainnet.infura.io/v3/e682a2332362431cbff2af376b64faeb"
    web3 = Web3(Web3.HTTPProvider(infura_url))
    is_connected = web3.isConnected()

    return render(request, 'portfel.html', { 'is_connected': is_connected })

def ceny(request):
    if request.method == 'POST':
        zapytanie = request.POST['zapytanie']
        krypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + zapytanie + "&tsyms=PLN")
        krypto = json.loads(krypto_request.content)
        cena_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BAT&tsyms=PLN")
        cena = json.loads(cena_request.content)
        return render(request, 'ceny.html', {'cena': cena, 'zapytanie': zapytanie, 'krypto': krypto })

    else:
        cena_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BAT&tsyms=PLN")
        cena = json.loads(cena_request.content)
        return render(request, 'ceny.html', {'cena': cena })


def blog(request):
    news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    news = json.loads(news_request.content)
    # jprint.jprint(news)
    return render(request, "blog.html", {'news': news })
    

def wydarzenia(request):
    
    url = "https://developers.coinmarketcal.com/v1/events"
    querystring = {"max":"20", "sortBy": "hot_events"}
    payload = ""
    headers = {
        'x-api-key': "tf7dkXjJQo9YUHH3PL5Flt0ShmJlcIf2OmWh1Mk0",
        'Accept-Encoding': "deflate, gzip",
        'Accept': "application/json"
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    event_cal = json.loads(response.content) 
    # print(event_cal)

    # jprint.jprint(event_cal)



    return render(request, "wydarzenia.html", {'event_cal': event_cal})