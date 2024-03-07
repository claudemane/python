import os
path = input("input your path:")
try:
    if os.path.exists(path):
        os.remove(path)
        print(f"{path} has been deleted")
    else:
        print(f"Path '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied for the path '{path}'.")
