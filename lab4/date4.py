from datetime import *
d1 = str(input("Input 1st date:"))
d2 = str(input("Input 2nd date:"))
date1 = datetime.strptime(d1, "%d/%m/%Y")
date2 = datetime.strptime(d2, "%d/%m/%Y")
print(abs(date1 - date2).days * 3600 * 24)