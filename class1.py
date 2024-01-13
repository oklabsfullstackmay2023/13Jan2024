#1 class ddefination is one time process
class MyClass():
    #1 Property/Variable
    name=''#define
    surname=''#define

    #2 Construtor/Esp. Defination/Method/Function
    def __init__(self):
        self.name="Kailash" #Initialize
        self.surname="Mahawar" #Initialize
        pass

    #3 Method / Function
    def getMyFullName(self):
        print(f'{self.name} {self.surname}')
        pass
    pass
#2. create class object
ceo1=MyClass()
print(ceo1.name) #Access
print(ceo1.surname) #Access
ceo1.getMyFullName()

