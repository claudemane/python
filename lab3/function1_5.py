def znaki(a):
    b = ",.!?;:-_()"
    c = ""
    for i in a:
        if(i in b):
            c += i
    print(c)
a = input()
znaki(a)

