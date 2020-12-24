from matplotlib import pyplot as plt
import Point as po


class Points:

    Ptr = []
    a = po.A
    b = po.B

    def __init__(self, n):

        for i in range(n):

            P = po.Point()
            P.newRandPoint(0, min(self.a, self.b))

            while P in self.Ptr:
                P.newRandPoint(0, min(self.a, self.b))

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
        plt.plot(X, Y, 'ro', color='white')
        plt.axis([0, self.a, 0, self.b])
        self.axi = plt.axes()
        self.axi.set_facecolor('black')
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