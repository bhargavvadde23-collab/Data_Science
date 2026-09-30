'''Encapsulation
Encapsulation in oops is the concept of wrapping the data members and methods together
in to a single unit retrict some direct access to the objects
'''
#preventing isuse of data


#it can be achieved by using getter and setter methods Nd 
#public , private __ , protected _



#for understanding
#Ex-1
'''
class Person:
    def __init__(self,name,age):
        self.name=name      #public variable
        self.age=age        #public variable
        
def get_info(person):           #this method can access outside the class
    return person.name

p=Person('bhargav',22)
print(get_info(p))

'''


#Ex-2
'''
class Person:
    def __init__(self,name,age):
        self.__name=name      #private variable
        self.__age=age        #private variable
        
def get_info(person):           #this method cannot access outside the class results in error
    return person.name

p=Person('bhargav',22)
print(get_info(p))
'''


#We can use private variables by using the getter and setter methods
'''
class Person:
    def __init__(self,name,age):
        self.__name=name      #public variable
        self.__age=age        #public variable
        
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name=name
    
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("negative number")

p=Person('bhargav',22)

print(p.get_name())
print(p.get_age())

#Modifying private variables 

p.set_name('king')
print(p.get_name())
p.set_age(20)
print(p.get_age())

'''




#Protected - protected variables can be used in derived classes only
'''
class Person:
    def __init__(self,name,age):
        self._name=name      
        self._age=age  
        
class Employee(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        
emp=Employee("bhargav",20)
print(emp._name) 
'''   

