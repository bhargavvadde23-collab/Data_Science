#Ex-1
#Opening a file
'''
with open("example.txt","r") as file:
    content=file.read()
    
    print(content)
'''

#Ex-2

'''
with open("example.txt","r") as file:
    for line in file:
        print(line.strip())             #it skips the newline character strip()
'''




#Appending to a file
'''
with open("example.txt","a") as file:
    file.write("\nthis is a new line")
'''



#Ex-1
'''
line=['\nfirst line\n','second line\n','third line']

with open("example.txt","a") as file:
    file.writelines(line)
'''
    

    
#Writing to a file means overwriting the entire file, it deletes prvious text
'''
with open("example.txt","w") as file:
    file.write("i have overwritten the existing file\n")
    file.write("this is a new begining")

'''



#Ex---w+ mode
'''
with open("exapmle2.txt","w+") as file:
    file.write("this is a new file\n")
    file.write("welcome\n")
    
    #seek(0) is used to move the cursor to the beginnnig 
    file.seek(0)               #without this content will not be printed in the terminal
    content=file.read()
    print(content.strip())
'''



