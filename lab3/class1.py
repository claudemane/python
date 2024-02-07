class string:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Please enter a string: ")

    def printString(self):
        print(self.string.upper())

obj = string()
obj.getString()
obj.printString()