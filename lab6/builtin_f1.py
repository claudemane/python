b = input("Input your list:").split()
a = [int(i) for i in b]
for i in range(len(a)):
    a[i] *= 2
print(f"Result: {a}")
