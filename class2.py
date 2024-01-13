#1 class defination is one time process
class MyClass():
    #1. Property/Variable
    name="" # Define
    surname="" #define 
    
    #2. Constructor/Esp. defination/method/function
    def __init__(self):
        self.name="Dinesh" # Initialize
        self.surname="Mahawar" # Initialize
        pass

        #3.1 Method/Function
    def getMyFullName(self):
        print(f'{self.name} {self.surname}')
        pass

    pass
#2 create class object is many time process
ceo1=MyClass()

print(ceo1.name) #Access
print(ceo1.surname) #Access

ceo1.getMyFullName()