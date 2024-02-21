def squares(a,b):
    for i in range(a, b):
        yield i * i
a = int(input())
b = int(input())
for i in squares(a,b):
    print(i)