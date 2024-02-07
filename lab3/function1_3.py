def solve(numheads, numlegs):
    rabits = (numlegs - 2 * numheads) / 2
    chickens = numheads - rabits
    print("Number of rabbits:",int(rabits))
    print("Number of chickens:", int(chickens))
legs, heads =int(input("Number of legs: ")), int(input("Number of heads: "))
solve(heads,legs)