'''
Inheritance in oops is a concepts that allows a class to inherit attributes and methods for 
another class
'''


#Singel level inheritance

'''
class Car:
    def __init__(self,windows,doors,engine_type):
        self.windows=windows
        self.doors=doors
        self.engine_type=engine_type
        
    def drive(self):
        print(f"person driving {self.engine_type} car")

car1=Car(4,5,'petrol')
car1.drive()

class Tesla(Car):
    def __init__(self,windows,doors,engine_type,is_selfdriving):
        super().__init__(windows,doors,engine_type)
        self.is_selfdriving=is_selfdriving
        
    def selfdriving(self):
        print(f"tesla supports selfdriving :{self.is_selfdriving}")
            
tesla=Tesla(4,5,"electric",True)
tesla.drive()
tesla.selfdriving()
'''





#Multilevel inheritance

'''
class Animal:
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        print("this is 1st parent method")
        
class Pet:
    def __init__(self,owner):
        self.owner=owner
        
class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
        
    def speak(self):
        print(f"this is sub class")
        
dog1=Dog("buddy","bhargav")
dog1.speak()

'''
