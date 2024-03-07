import os
path = input("input your path:")
try:
    print("Directories:")
    for dir_name in os.listdir(path):
        dir_path = os.path.join(path, dir_name)
        if os.path.isdir(dir_path):
            print(dir_name)

    print("\nFiles:")
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path):
            print(file_name)

    print("\nAll Directories and Files:")
    for item_name in os.listdir(path):
        item_path = os.path.join(path, item_name)
        print(item_name)
        
except FileNotFoundError:
    print(f"The specified path '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied for the path '{path}'.")
