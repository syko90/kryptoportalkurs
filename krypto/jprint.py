import json 

def jprint(krypto):
    # tworzy sfromatowany JSON  postaci string
    text = json.dumps(krypto, sort_keys=True, indent=4)
    print(text)