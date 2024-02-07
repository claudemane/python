def reversewords(a):
    b = []
    b += a[::-1]
    return b
a = input().split()
print(" ".join(reversewords(a)))