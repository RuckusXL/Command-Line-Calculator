#This script is practice for working with directories and file paths. It will create a new directory, change into that directory, create a new file, write some text to that file, read the contents of the file, and then delete the file and the directory. This script is intended for educational purposes and should not be used in production environments.
#This script is for educational purposes only and should be used as a learning tool for understanding basic file and directory operations in Python. It is not intended for production use and may not include error handling or best practices for file management.
#Author: RuckusXL

import os
import shutil
from datetime import datetime

#Print the current working directory
def print_cwd():
    cwd = os.getcwd()
    print(f"\nDirectory: {cwd}")

#Change to a new directory
def change_dir(new_dir):
    os.chdir(new_dir)
    print(f"\nChanged to: {new_dir}")

#Print the contents of the current directory
def list_dir():
    contents = os.listdir()
    print(f"\nContents: {contents}")
    
    return contents

#Create a new folder in current directory and navigate into it
def create_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)
    print(f"\nCreated new folder: {folder_name}")
    change_dir(folder_name)

#Create a new file
def new_file(file_name):
    with open(file_name, "w") as file:
        file.write("This is a new file created on " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(f"\nCreated new file: {file_name}")

#Move a file(s) from one directory to another
def move_file(source, destination):
    shutil.move(source, destination)
    print(f"\nFile successfully moved from {source} || {destination}")

#Remove a directory
def del_dir(dir_name):
    shutil.rmtree(dir_name)
    print(f"\n{dir_name} successfully deleted.")

#Delete a file
def del_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"\nThe file {file_name} has been deleted.")
    else:
        print(f"\nThe file {file_name} does not exist.")

    
print_cwd()
change_dir(os.path.join(os.path.expanduser("~"), "Desktop"))
list_dir()
create_folder("test_folder")
new_file("test_file.txt")
move_file(os.path.join(os.path.expanduser("~"), "Desktop", "test_folder", "test_file.txt"), os.path.join(os.path.expanduser("~"), "Desktop", "test_file.txt"))
change_dir(os.path.join(os.path.expanduser("~"), "Desktop"))
del_dir("test_folder")
del_file("test_file.txt")
