def uniq(list):
    uniqlist = []
    for i in list:
        t = True
        for j in uniqlist:
            if(i == j):
                t = False
                break
        if(t):
            uniqlist.append(i)
    print(" ".join([str(i) for i in uniqlist]))
list =[int(i) for i in input().split()]
uniq(list)