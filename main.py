import math
import numpy as np
import random
from matplotlib import pyplot as plt
from matplotlib import animation

A = 30 # columns
B = 30 # rows

fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line = ax.plot([], [], lw=2)

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

class Points:

    Ptr = []
    a = A
    b = B

    def __init__(self, n):

        for i in range(n):

            P = Point()
            P.newRandPoint(0, min(A, B))

            while P in self.Ptr:
                P.newRandPoint(0, min(A, B))

            w = P.retPoint()
            self.Ptr.append(w)

    def add(self, x, y):
        self.Ptr.append((x, y))

    def retPtr(self):
        return self.Ptr

    def numOfNeighbors(self, point, a, b):
        n = 0
        p = point.retPoint()
        if p == (0, 0):
            if self.isPoint(1, 0):
                n += 1
            if self.isPoint(1, 1):
                n += 1
            if self.isPoint(0, 1):
                n += 1
        elif p == (0, b):
            if self.isPoint(1, b):
                n += 1
            if self.isPoint(0, b-1):
                n += 1
            if self.isPoint(1, b-1):
                n += 1
        elif p == (a, 0):
            if self.isPoint(a-1, 0):
                n += 1
            if self.isPoint(a-1, 1):
                n += 1
            if self.isPoint(a, 1):
                n += 1
        elif p == (a, b):
            if self.isPoint(a-1, b):
                n += 1
            if self.isPoint(a-1, b-1):
                n += 1
            if self.isPoint(a, b-1):
                n += 1
        else:
            xP = p[0]
            yP = p[1]

            if self.isPoint(xP-1, yP):
                n += 1
            if self.isPoint(xP-1, yP+1):
                n += 1
            if self.isPoint(xP-1, yP-1):
                n += 1
            if self.isPoint(xP, yP-1):
                n += 1
            if self.isPoint(xP, yP+1):
                n += 1
            if self.isPoint(xP+1, yP):
                n += 1
            if self.isPoint(xP+1, yP+1):
                n += 1
            if self.isPoint(xP+1, yP-1):
                n += 1

        return n

    def create(self):
        X = [x[0] for x in self.Ptr]
        Y = [x[1] for x in self.Ptr]
        plt.plot(X, Y, 'ro')
        plt.axis([0, A, 0, B])
        plt.show()

    def isPoint(self, x, y):
        if (x,y) in self.Ptr:
            return True
        return False

    def search(self, x, y):
        for i in range(len(self.Ptr)):
            if self.Ptr[i] == (x, y):
                return i

        return -1

    def deletePoint(self, x, y):
        self.Ptr.remove((x, y))

class Game:

    p = Points(50)
    point = Point()
    a = A
    b = B

    def __init__(self):
        self.p.create()

    def nextGeneration(self):

        for x in range(self.a+1):
            for y in range(self.b+1):

                if (x,y not in self.p.Ptr):
                    self.point.newPoint(x, y)
                    n = self.p.numOfNeighbors(self.point, self.a, self.b)

                    if n == 3:
                        self.p.add(x, y)


        for x in range(self.a+1):
            for y in range(self.b+1):
                if (x,y) in self.p.Ptr:
                    self.point.newPoint(x, y)
                    n = self.p.numOfNeighbors(self.point, self.a, self.b)

                    if (n < 2 or n > 3):
                        self.p.deletePoint(x, y)

        self.play()
        return self.p.Ptr


    def play(self):
        self.p.create()



