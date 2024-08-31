#1. Exploring Python's OS Module
#Task 1: Directory Inspector:
#Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. 
#Your script should prompt the user for the directory path and then display the contents.

import os

def list_directory_contents(path): # List and print all files and subdirectories in the given path
    try:
        for directory, subdirectory, files in os.walk(path): # roots within repository
            directory = os.path.basename(directory) # gets the name of file instead of path
            print(f"Directory: {directory}")
            for subdir_name in subdirectory:
                subdir_name = os.path.basename(subdir_name) # gets name of file instead of path
                print(f"- Subdirectory: {subdir_name}")
            for file_name in files:
                print(f"- File: {file_name}")
    except Exception as e:
        print(f"Error: {e}. Please try again")
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Error, check file permissions and try again")
path = os.getcwd() # pulls the current working directory 
list_directory_contents(path)
