import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        print(math.sqrt(dx**2 + dy**2))
point = Point(int(input()), int(input()))
point.show()
point.move(int(input()), int(input()))
point.show()
p = Point(int(input()), int(input()))
point.dist(p)