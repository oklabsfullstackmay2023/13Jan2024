#1 class defination is one time process
class MyClass():
    #1. Property/Variable
    name="" #define
    surname="" #define
    pass

    #2. Constructor/Esp.Function
    def __init__(self):
        self.name="Pooja" #Initialize
        self.surname="Mahawar" #Initialize
        pass

    #3. Method/Function
    def getMyFullName(self):
        print(f'{self.name} {self.surname}')
        pass
    pass
#2 create class object is many time process
ceo1=MyClass()

print(ceo1.name) #Access
print(ceo1.surname) #Access

ceo1.getMyFullName()