from django.shortcuts import render
import requests
import json
from . import jprint


# Create your views here.
# def wyszukiwarka(request):
#     if request.method == "POST":
#         zapytanie = request.POST['zapytanie']
#         print(zapytanie)
#         krypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms= " + zapytanie + "&tsyms=PLN")
#         krypto = json.loads(krypto_request.content)
#         return render(request, 'ceny.html', { 'zapytanie': zapytanie, 'krypto': krypto} )
#     else: 
#         return render(request, 'ceny.html')

def ceny(request):
    if request.method == 'POST':
        zapytanie = request.POST['zapytanie']
        print(zapytanie)
        krypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + zapytanie + "&tsyms=PLN")
        krypto = json.loads(krypto_request.content)
        cena_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BAT&tsyms=PLN")
        cena = json.loads(cena_request.content)
        return render(request, 'ceny.html', { 'zapytanie': zapytanie, 'krypto': krypto, 'cena': cena} )

    else:
        cena_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BAT&tsyms=PLN")
        cena = json.loads(cena_request.content)
        jprint.jprint(cena)
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