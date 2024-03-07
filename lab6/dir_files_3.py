import os
path = input("Input your path:")
try:
    if os.path.exists(path):
        print(f"Path '{path}' exists.")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"Path '{path}' does not exist.")

except PermissionError:
    print(f"Permission denied for the path '{path}'.")
