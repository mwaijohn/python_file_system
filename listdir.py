import os
#list all directories in a particular path and write them into a text file
path = input("Enter the path to list directories: ")
ile = path + "/directories.txt"
if os.path.exists(path):
   f = open(ile,'w')
   dirs = os.listdir(path)
   for fg in range(len(dirs)):
    f.write(str(dirs[fg]))
    f.write("\n")
   f = open(ile,'r')
   for g in f.readlines():
       print(g)
   print("The path to the directory.txt is " +ile)
   print("items were successifully written to the file")
else:
    print("The path does not exist")
