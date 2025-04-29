#The fountain v1
from fluttershy.fetch import getResponseJD
# from fountain.dime import Fountain as fate
from engine.engine import Engine
import time
class Fountain:
    def __init__(self):
        self.per=None
        self.dime=None
        self.chDime=None
        self.newValue=None

    #Take the dime's value here
    def takeDime(self):
        self.dime=float(input("Enter the value of the Dime here: "))
        return self.dime

    #Percentage Delta, this thing calculates the difference in percentage
    def perdel(self, value1, value2):
        self.value1=value1
        self.value2=value2
        self.per=(((self.value2-self.value1)/self.value1)*100)
        return self.per
    
    def change(self):
        self.chDime= ((self.per/100)*self.dime)
        return self.chDime
    
    def DimeLater(self):
        self.newValue = self.chDime + (self.dime)
        return self.newValue
    
fate = Fountain()

data = getResponseJD()
btc = data['bitcoin']['inr']
time.sleep(60)
data2 = getResponseJD()
btc2 = data2['bitcoin']['inr']

print(f"First: {btc}, Second: {btc2}")

dime=fate.takeDime()
per=fate.perdel(btc, btc2)
chDime=fate.change()
newValue=fate.DimeLater()

print("Change percentage: ", per)
print("Dime taken: ", dime)
print("New dime: ", newValue)
print("Change in dime: ", chDime)

