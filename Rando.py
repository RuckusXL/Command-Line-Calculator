#Author: RuckusXL
import os

#This function will take user input of a filepath
def userinput():
    filepath = input("\nInput from the user: ").strip().strip('"')
    return filepath

#This function will list the content of the current directory
def list_dir(directory):
    see = os.listdir(directory)
    filetype = (".txt", ".py")
    matches = []
    
    for line in see:
        for word in filetype:
            if word.lower() in line.lower():
                matches.append(line)
                break
    return(matches)

#This function will attempt to extract the contents from a file and print them onto another file
def borrow_letters(filenames, directory):
    output_path = os.path.join(directory, "combined_output.txt")

    with open(output_path, "w", encoding="utf-8") as outfile:
        for filename in filenames:
            fullpath = os.path.join(directory, filename)

            if filename.lower().endswith((".txt", ".py")):
                with open(fullpath, "r", encoding="utf-8") as infile:
                    outfile.write(f"\n--- {filename} ---\n")
                    outfile.write(infile.read())

filepath = userinput()
spygames = (list_dir(filepath))
borrow_letters(spygames, filepath)