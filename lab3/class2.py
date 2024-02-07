class Shape:
    def __init__(self):
        pass

    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length

    def area(self):
        print(self.length*self.length)
square = Square(int(input()))
square.area() 
shape = Shape()
shape.area()
