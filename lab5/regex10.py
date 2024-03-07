import re
s = input()
def deff(a):
    return a.group(0)[0] + "_" + a.group(0).lower()[1]
ss = re.sub('(.)[A-Z]', deff, s)
print(ss)
