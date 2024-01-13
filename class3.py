#1 class defination is one time process
class MyClass():
    #1. Property/Variable
    name='' #Define
    surname='' #Define
    pass

    #2. Constructor/Esp.Function
    def __init__(self):
        self.name="Anita" #Initialize
        self.surname="Mahawar" #Initialize
        pass

    #3. Method/Function
    def getMyFullName(self):
        print(f'{self.name} {self.surname}')
        pass
    pass
#2 create class object is many time process
ceo1=MyClass()

print(ceo1.name) #access
print(ceo1.surname) #access

ceo1.getMyFullName()