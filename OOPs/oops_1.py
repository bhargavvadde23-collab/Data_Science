#understanding the constructor
#constructer is called whenever the object is created
#self is a keyword refers to the current object
#init is the constructor of the class
#Ex-1
'''
class Student:
    def __init__(self):
        print("Constructer created")
        
s1=Student()
'''


#Ex-2
'''
class Student:
    def __init__(self,name):
        self.name=name
        
    def display(self):
        print(self.name)

s1=Student("bhargav")
s1.display()
'''



#Ex-3
'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        print("Name:",self.name,"\n","Age:",self.age)

s1=Student("bhargav",20)
s1.display()
'''

