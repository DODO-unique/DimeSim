#We take values and returns all calls-this module is for process management and arrangment
import csv

class Engine:
    def __init__(self, dime, per, chDime, newValue, key=False):
        self.per=per
        self.dime=dime
        self.chDime=chDime
        self.newValue=newValue
        self.key=key
    
    def initial_storing(self):
        with open('data.csv', 'r+', newline='') as file:
            # seek(0)
            writer = csv.writer(file)
            writer.writerows([['index', 'Dime', 'Percentage Change', 'Change in Dime', 'New Dime'], [1, self.dime, self.per, self.chDime, self.newValue]])
        # print("Change percentage: ", self.per)
        # print("Dime taken: ", self.dime)
        # print("New dime: ", self.newValue)
        # print("Change in dime: ", self.chDime)

    def logs(self, coin, percent, change_in_Dime, new_Dime, count):
        self.coin=coin
        self.percent=percent
        self.change_in_Dime=change_in_Dime
        self.new_Dime=new_Dime
        self.count=count
        with open('data.csv', 'a+', newline='') as file:
            writer2 = csv.writer(file)
            writer2.writerow([self.count, self.coin, self.percent, self.change_in_Dime, self.new_Dime])
