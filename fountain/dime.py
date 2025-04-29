#The fountain v1
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
        self.per=((self.value2-self.value1)/self.value1)*100
        return self.per
    
    #change in the dime
    def change(self):
        self.chDime= (self.per/100)*self.dime
        return self.chDime
    
    #new value of the dime
    def dimeLater(self):
        self.newValue = self.chDime + (self.dime)
        return self.newValue
    
    '''Note that the changes would be miniscule. Bitcoin is volatile, but not that volatile. Expect changes for big dime.'''
# fate = Fountain()

