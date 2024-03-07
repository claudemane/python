import re
s = input()
ss = re.findall("a{1}b{2}b?", s)
print(ss)
