def pal(a):
    x = len(a)
    t = True
    for i in range(0,x // 2):
        if(a[i] != a[x - 1 - i]):
            t = False
            break
    if(t):
        print("Palindrome")
    else:
        print("Not palindrome")
pal(input())
