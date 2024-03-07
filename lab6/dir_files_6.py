name = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = ".txt"
for i in name:
    file = open(i + t, "x")
    file.close()
