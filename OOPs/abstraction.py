'''Abstraction
Abstraction in oops is a concept of hiding the complex implementation details and showing the 
only necessary objects . this helps in reducing programmin complexity and effort
'''



from abc import ABC,abstractmethod

class Vehicle(ABC):
    def start(self):
        print("this vehicle is running")
        
    @abstractmethod
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        print("this is car engine")
        
def print_engine(vehicle):
    vehicle.start_engine()
    vehicle.start()
    
c=Car()
print_engine(c)
