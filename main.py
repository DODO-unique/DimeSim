from fluttershy.fetch import getResponseJD
from fountain.dime import Fountain as fate
from engine.engine import Engine
import time

data = getResponseJD()
btc = data['bitcoin']['inr']
time.sleep(10)
data = getResponseJD()
btc2 = data['bitcoin']['inr']

fate=fate()
dime=fate.takeDime()
per=fate.perdel(btc, btc2)
chDime=fate.change()
newValue=fate.dimeLater()

en = Engine(dime, per, chDime, newValue, True)

en.initial_storing()

print("Entering call loop, press ctrl+c to terminate the process: ")
#for loop calls
count=1

while True:
    time.sleep(10)
    
    print("\nFetching values", end="")

    for _ in range(3):
        time.sleep(1)
        print(".", end="" , flush=True)
    
    #flush variables for reuse
    per=0
    chDime=0
    newValue=0
    data=0
    coin=0

    #don't forget the counter
    count+=1

    #fetch from fluttershy
    data = getResponseJD()

    coin = data['bitcoin']['inr']

#Okay, so there are two ways to process coin: one, we send coin to engine and engine runs a function that does the same calculation but this time with the initial value and then returns everything which we immediately send from this loop to Pancakes which will handle outputs later and engine will also store things and calcs OR two, we can send this to Fountain that is our 'calc' hub and then fetch the data and then send it to Engine for storing logging processing and then collect that and send it to pancackes...
#We are going with two because it is more future proof, so contributes to MVP logic where minimal is viable and also gives foundation to next projects

    #sending the data to fountain.fate and fetching values
    per=fate.perdel(btc, coin)
    chDime=fate.change()
    newValue=fate.dimeLater()

    #logs in a csv file, check engine for reference
    en.logs(coin, per, chDime, newValue, count)


