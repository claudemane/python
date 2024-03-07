a = input("Input your string:")
lows = 0
ups = 0
for i in a:
    if i.islower():
        lows += 1
    elif i.isupper():
        ups += 1
print(f"Number of lower case letters: {lows}")
print(f"Number of upper case letters: {ups}")
