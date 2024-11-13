import os

def print_directory_contents(path):
    try:
        # List all files and directories in the specified path
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print("The specified directory does not exist.")
    except PermissionError:
        print("Permission denied to access the specified directory.")

# Specify the path to the directory
directory_path = '.'  # Current directory
print_directory_contents(directory_path)
