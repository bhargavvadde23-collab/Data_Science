'''
#getting the absolute path i recommend this

import os

file_name="example.txt"
absolute_path=os.path.abspath(file_name)
print(absolute_path)
'''





#Getting the absolute full path
'''
import os

dir_name="File handling"
file_name="example.txt"
full_path=os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)
'''



#To create a new directory
'''
import os

new_dir=("Package")
os.mkdir(new_dir)

print(f"new directory is {new_dir}")
'''



