'''
Exception handling

Exception handling in python allowa you to handle errors gracefully and take corrective 
actions without stopping the execution of python.

What are exceptions

exceptions are events in program that disrupts the flow of program. they occur when the 
error is encountered in the program

Most common errors are

ZeroDivisionError : divided by zero
FileNotFoundError  :File is not found
ValueError          :invalid value
TypeError           :invalid type
'''




'''
#Normal way

try:
    a=b
    
except Exception:
    print("check once again")
    
#if we know the Exception 

try:
    a=b
except NameError as ex:
    print(ex)
    
try:
    a=1/0
except ZeroDivisionError as ex:
    print(ex)
    
except Exception as ex1:
    print(ex1)
    print("it is the main exception")     # Do not write before exceptions
    
#Therefore handling the errors carefully
'''




'''
#Value error

try:
    num=int(input("enter a number: "))
    result=10/num
except ValueError as ex:
    print(ex)
except ZeroDivisionError as ex1:
    print(ex1)
'''




'''
#try and else


try:
    num=int(input("enter a number: "))
    result=10/num
except ValueError as ex:
    print(ex)
except ZeroDivisionError as ex1:
    print(ex1)
else:
    print(result)
'''



'''

#Try , except, else , finally

try:
    num=int(input("enter a number: "))
    result=10/num
except ValueError as ex:
    print(ex)
except ZeroDivisionError as ex1:
    print(ex1)
else:                                   #it'll executes if the error not occurs
    print(result)
    
finally:                                #it'll execute if the error occurs  and not occurs
    print("execution complete")
'''



'''

#File not found error

try:
    file=open("example.txt","r")            #it exists
    content=file.read()
    print(content)
    
except FileNotFoundError as ex:
    print(ex)
    
finally:
    print("execution complete")
'''
