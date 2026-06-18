#This started out as a study script. Just me messing around writing a script that moves around directories and add text and extracts text
#As I was extracting data, I said hey I bet this is how log readers work. So this ended up becoming a full fledge log reading project
#Day 10
#Author: RuckusXL

import os

#This function navigates to a desired filepath and prints it
def get_filename():
    filename = input("Filepath: ").strip().strip('"')
    return filename

#This function writes to a new or existing file on desktop
def onthetop(filename):
    with open(filename, "a") as file:
        new_file = file.write("\nYou will, you will accept us\nGood we have so much work to do")
        new_file

#This function reads the contents of a file given the path to the file
def scan_file(filename):
    from datetime import datetime
    from colorama import Fore
    from colorama import init
    init(autoreset=True)    

    keywords = ["ERROR", "WARNING", "FAILED", "CRITICAL"]
    counts = {key: 0 for key in keywords}

    with open(filename, "r") as file:
        for line in file:
            lower_line = line.lower()
            
            for word in keywords:
                if lower_line.startswith(word.lower()):
                    counts[word] += 1

                    if word == "ERROR":
                        print(Fore.MAGENTA + line.strip())
                    elif word == "WARNING":
                        print(Fore.YELLOW + line.strip())
                    elif word == "CRITICAL":
                        print(Fore.RED + line.strip())
                    elif word == "FAILED":
                        print(Fore.BLUE + line.strip())

                    break

    print("\n--- Summary ---\n")
    for key, value in counts.items():
        print(f"{key}: {value}\n")


filename = get_filename()
#onthetop(filename)
scan_file(filename)