
#python3
#compare_folders.py

import os


print("Welcome to a program for synchronizing files between two directories")

source = input("Please enter the source directory path: ")

#See if the Source path exists
try:
  os.chdir(source)
except OSError:
  print("Error: Cannot open " + source)
  quit()



target = input("Please enter the target directory path: ")


#See if the target path exists
try:
  os.chdir(target)
except OSError:
  print("Error: Cannot open " + target)
  quit()


#List structure to hold all the file names
all_files_source = []
all_files_dest   = []


#Move to the source dir
os.chdir(source)
cwd = os.getcwd()
str_prefix = len(cwd)
#print("In directory: " + cwd + "\n\n")
for dir_path, dir_names, file_names in os.walk(cwd):
  for f in file_names:
    path = dir_path[str_prefix:] + '/' + f
    #print( path )  #tobe removed
    all_files_source.append(path) 


#Move to dest folder
os.chdir(target)
cwd=os.getcwd()
str_prefix = len(cwd)
#print("In directory: " + cwd + "\n\n")
for dir_path, dir_names, file_names in os.walk(cwd):
  for f in file_names:
    path = dir_path[str_prefix:] + '/' + f
    #print( path )  #tobe removed
    all_files_dest.append(path) 


print('\n\n')

missing = set(all_files_source).difference(all_files_dest)

if len(missing) == 0:
  print("The dest folder is synced with the source folder!")
else:
  print("Here are the missing files! \n")
  for x in missing:
    print(x)    
    
print('\n')






