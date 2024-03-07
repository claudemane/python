import os
path = input("Input your path: ")
try:
    if os.path.exists(path):
        print(f"Path '{path}' exists.")
    else:
        print(f"Path '{path}' does not exist.")

    file = open(path, "r")

    if file.readable():
        print(f"Path '{path}' is readable.")
    else:
        print(f"Path '{path}' is not readable.")

    if file.writable():
        print(f"Path '{path}' is writable.")
    else:
        print(f"Path '{path}' is not writable.")

    if os.access(path, os.X_OK):
        print(f"Path '{path}' is executable.")
    else:
        print(f"Path '{path}' is not executable.")
    file.close()
except FileNotFoundError:
    print(f"The specified path '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied for the path '{path}'.") 
