def gen():
    for i in range(int(input())):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for i in gen():  
    print(i)