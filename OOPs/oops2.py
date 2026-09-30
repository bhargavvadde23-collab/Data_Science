#OOPs concepts
#OOPc concept in python is a way of organisng the code using the classes and objects,
#The four main concepts of oops are encapsulation,inheritance,abstraction,polymorphism

#Encapsulation
#Wrapping the data members and the methods together and restricting the acces to some data
#it can be achieved in three ways 

#1)Public ---- can access from anywhere
'''
class Student:
    def __init__(self):
        self.name="bhargav"

s1=Student()
print(s1.name)
'''



#Protected -can acces within the class  variables and methods are created using "_"
'''
class Student:
    def __init__(self):
        self._name="bhargav"
        
s1=Student()
print(s1._name)
'''


#Private method is indicated using "__"
'''
class Student:
    def __init__(self):
        self.__name="bhargav"
        
    def display(self):
        print(self.__name)
        
s1=Student()
#print(s1.__name)    #Error
s1.display()
'''



#Inheritance
#We pass name of parent class as an parameter to the child class
#using methods
'''
class Person:
    def display(self):
        print("this is parent class")
        
class Student(Person):
    def show(self):
        print("this is child class")
        
s=Student()

s.display()
s.show()
'''


#using constructors
'''
class Student:
    def __init__(self):
        self.name="bhargav"
        
class person(Student):
    def show(self):
        print(self.name)
        
s=person()
s.show()
'''



#multilevel inheritance
'''
class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")
        
class C(A,B):
    pass

s=C()
s.showA()
s.showB()
'''



#Abstraction
#Declaring the abstract method in the parent class and implementing the details in the child class
#We should import abs , it is a built in python library which is used for declaring abstract methods and class
#abs = abstract base class
'''
from abc import ABC,abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass
    
class dog(Animal):
    
    def sound(self):
        print("barking")
        
class cat(Animal):
    
    def sound(self):
        print("meow")
        
c=cat()
d=dog()

c.sound()
d.sound()
'''


#Polymorphism  -- one interface many forms
#Method overriding
#Sound method is overridden by the child class
'''
class Animal:
    def sound(self):
        print("bark")
        
class cat(Animal):
    def sound(self):
        print("meow")
        
c=cat()
c.sound()
'''



