from time import sleep
from math import sqrt
n = int(input("Input your number:"))
t = int(input("Input your time:"))
n2 = sqrt(n)
sleep(t / 1000)
print(f"Square root of {n} after {t} miliseconds is {n2}")
