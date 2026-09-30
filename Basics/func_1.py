#Functions in python are blocks of code designed to do specific task,improves readability,reusability
#There are different types of functions are used in python
#1)Function with Default parameters
#2)Funtion with no parameters
#3)funtion with return values
#4)Funtion with Positional arguments
#5)Funtions with Keyword arguments


#Default
'''
def greet(name="amigo"):
    print(f"hello {name} ,Welcome")
    
greet()         #greet("bhargav") it prints bhargav
'''


#Variable lentgh arguments
#Positional arguments
'''
def greet(*args):
    for num in args:
        print(num)
        
greet(1,2,3,4,5,"messi")
'''

#Keyword arguments
'''
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
print_details(name="bhargav",age=22,grade='A')
'''



#Function to convert temparature to farenheit and vice versa
'''
def convert(temp,unit):
    if unit=='C':
        return temp*9/5 +32     #celcius to farenheit
    elif unit=='F':
        return (temp-32)*5/9    #farenheit to celcius
    else:
        return None

print(convert(25,'C'))
print(convert(77,'F'))
'''




#Strong password function
'''
def is_strong(password):
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$&*()_+' for char in password):
        return False
    else:
        return True
    
print(is_strong("Weakpwd"))
print(is_strong("Strong1!"))
'''




#total cost in a cart
'''
def total_cost(cart):
    total=0
    
    for item in cart:
        total+=item["price"]*item["quantity"]
        
    return total

cart=[
    {'name':"apple",'price':0.4,'quantity':4},
    {'name':'banana','price':0.5,'quantity':5},
    {'name':'carrot','price':0.3,'quantity':3}
] 

print(total_cost(cart))
'''




#lambda and map function ----without using a loop to iteration we an get every element in list

#lambda functions are small anonymous function defined using lamba key word . they can have any
#-number of arguments but only one expression .they are commonly used for short operations 

'''
even = lambda num:num%2==0
print(even(12))

add=lambda a,b,c:a+b+c
print(add(1,2,3))

print(type(even))
print(type(add))
'''




#Map ()- applies functions to all items in a list


#implementing map using lambda
'''
numbers=[1,2,3,4]
print(list(map(lambda num:num**2,numbers)))


#implementing map using a function

def square(num):
    return num**2

print(list(map(square,numbers)))
'''

#Map with multiple iterables
'''
num1=[1,2,3]
num2=[4,5,6]

print(list(map(lambda x,y:x+y,num1,num2)))
'''

#convert list of strings in to list of integer using map
'''
num3=['1','2','3']

print(list(map(int,num3)))
'''



#Ex
'''
def get_name(person):
    return person['name']

person=[
    {'name':'bhargav','age':22},
    {'name':'krishna','age':22}
]
print(list(map(get_name,person)))
'''


'''
Filter () --is a powerful tool for filtering the items in a list or in a dictionary
it is commonly used for data cleaning , filtering objects , and removing unwanted elements from the list

'''

#Ex-1

#filter using function
'''
def even(num):
    return num%2==0

lst=[1,2,3,4,5,6,7,8,9]
print(list(filter(even,lst)))


#filter using lambda

print(list(filter(lambda num:num>5,lst)))

print(list(filter(lambda num:num>5 and num%2==0 , lst)))
'''




def age_greater_25(person):
    return person['age']>25

person=[
    {'name':'bhargav','age':26},
    {'name':'krishna','age':22},
    {'name':'john','age':27}
]

print(list(filter(age_greater_25,person)))

