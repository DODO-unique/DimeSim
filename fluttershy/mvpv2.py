import requests
import time

def getResponseJD():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr"
    response=requests.get(url)
    dic=response.json()
    dic['timestamp']=int(time.time())
    return dic

print(getResponseJD())
'''this gives json response like { 'bitcoin': {'inr': value}, 'timestamp': epoch}'''
