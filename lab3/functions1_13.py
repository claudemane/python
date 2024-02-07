import random
num = random.randint(1, 20)
name = input("Hello! What is your name?\n")
print("Well, "+ name +", I am thinking of a number between 1 and 20.")
c = 0
while True:
    guess = int(input("Take a guess.\n"))
    c += 1
    if(guess < num):
        print("Your guess is too low")
        continue
    elif(guess > num):
        print("Your guess is too big")
        continue
    else:
        print("Good job, "+ name +"! You guessed my number in", c, "guesses!")
        break