import requests

def getResponseJD():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr"
    response=requests.get(url)
    return response.json()


'''this gives json response like { 'bitcoin': {'inr': value}}'''