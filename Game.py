import Points as pos
import Point as po


class Game:

    p = pos.Points(50)
    point = po.Point()
    a = po.A
    b = po.B

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