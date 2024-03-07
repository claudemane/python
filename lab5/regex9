import re
s = input()
def deff(a):
    return a.group(0)[0] + " " + a.group(0)[1]
ss = re.sub('(.)[A-Z]', deff, s)
sss = re.sub(r'([A-Z])([A-Z])', r'\1 \2', ss)
print(sss)
