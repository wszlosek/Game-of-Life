import random

A = 30
B = 30

def randomN(a, b):
    return random.randint(a, b)

class Point:

    x = 0
    y = 0

    def newPoint(self, a, b):
        self.x = a
        self.y = b

    def newRandPoint(self, a, b):
        self.x = randomN(a, b)
        self.y = randomN(a, b)

    def retPoint(self):
        return (self.x, self.y)