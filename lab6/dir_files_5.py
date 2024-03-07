a = [str(i) for i in input("input your list:")]
file = open("listtofile.txt", "w")
for i in a:
    file.write(i)
file.close()
with open("listtofile.txt", "r") as file:
    print(file.read())
