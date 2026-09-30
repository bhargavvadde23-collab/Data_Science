'''iterators are advanced python concept that allow efficient looping and memory management
'''


#Same goes for the strings also
'''
my_list=[1,2,3,4,5,6]

iterator=iter(my_list)

print(next(iterator))
print(next(iterator))
'''


#Decorators
#Passing the function as a parameter to the another function
#it adds the functionality to the function  without changing the actual code
#Ex-1
'''
def func1(func):
    def sub():
        print("this is a line1")
        func()
        print("this is a line 2")
        
    return sub

@func1
def say_hello():
    print("hello")
    
say_hello()
'''


