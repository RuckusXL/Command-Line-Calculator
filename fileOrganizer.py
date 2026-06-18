#This script organizes files on the desktop into folders based on their file extensions. It creates folders for Python files, text files, media files, and image files, and moves the corresponding files into these folders.
#This script is for educational purposes only and should be used as a learning tool for understanding basic file operations in Python. It is not intended for production use and may not include error handling or best practices for file management.
#This script was created with the help of ChatGPT and is a collaborative effort between the author and the AI. The author provided the initial idea and structure for the script, while ChatGPT assisted with writing the code and providing suggestions for improvements.
#Day 5 python project.
#Author: RuckusXL & ChatGPT

import os
import shutil

#Organize files on the desktop into folders based on their file extensions
def isit_mom():
    base_path = os.path.join(os.path.expanduser("~"), "Desktop")

    folders = {
        "Python": [".py"],
        "Text files": [".txt" , ".pdf"],
        "Media1": [".mp4", ".mkv", ".mp3"],
        "Images1": [".jpg", ".png"]
    }

    # Create folders if they don’t exist
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    # Loop through files
    for file in os.listdir(base_path):
        file_path = os.path.join(base_path, file)

        if os.path.isfile(file_path):
            for folder, extensions in folders.items():
                if file.endswith(tuple(extensions)):
                    destination = os.path.join(base_path, folder, file)
                    shutil.move(file_path, destination)
                    print(f"Moved {file} → {folder}")
                    break

isit_mom()


os.path.join(path1, path2)