'''polymorphism
Polymorphism is a oops concept that provides a way to perform a single action into different forms
polymorphism means many forms
it can be aceived through method overriding and method over loading
'''



'''Polymorphism in oops allowa flexibility and integration in code design it enables single fun
ction to handel different objects of different classes'''






#Ex-1

'''
class Animal:
    def speak(self):
        print("sound of animal")
        
class Dog(Animal):
    def speak(self):
        return "woof"
    
class Cat(Animal):
    def speak(self):
        return "meow"
    
dog=Dog()
print(dog.speak())
a=Animal()
a.speak()
c=Cat()
print(c.speak())

'''



#Ex-2
'''
class Shape:
    def area(self):
        print("area of this shape")

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius *self.radius
    
    
def print_area(shape):
        print(f"area {shape.area()}"  )
        
r=Rectangle(4,5)
c=Circle(4)
print_area(c)
print_area(r)

'''





#Abstract classes

#ABC abstract base class is used to define common methods for a group of related objects


from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Bike(Vehicle):
    def start_engine(self):
        return "bike started"
    
class Car(Vehicle):
    def start_engine(self):
        return "car started"
    
def print_engine(start):
    print(f"{start.start_engine()}")
    
b=Bike()
c=Car()
print_engine(b)
print_engine(c)
    
    
