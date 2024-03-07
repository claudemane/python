path = input("Input your path:")
with open(path, "r") as f:
    file = f.read()
n = 0
for x in file:
    n+=1
print(f"Number of lines: {n}")
