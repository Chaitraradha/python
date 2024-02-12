import os
#to get PWD
print(os.getcwd())
#to create a directory
os.makedirs("newdir",exist_ok=True)
#ls -lt
print(os.listdir("/home/ubuntu/newdir"))
#to change directory
print(os.chdir("/home/ubuntu/newdir"))
print(os.getcwd())
#to print whether file, if it is file it will print true
print(os.path.isfile("p1.py"))                          
#to print whether directory, if it is file it will print true
print(os.path.exists("newdir"))
print(os.path.basename("p1.py"))
