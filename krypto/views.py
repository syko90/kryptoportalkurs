from django.shortcuts import render
import requests
import json

# Create your views here.
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

    def jprint(krypto):
        # tworzy sfromatowany JSON  postaci string
        text = json.dumps(krypto, sort_keys=True, indent=4)
        print(text)

    jprint(event_cal)


    return render(request, "wydarzenia.html", {'event_cal': event_cal})