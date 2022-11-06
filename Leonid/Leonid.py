class human:
    def __init__(self, a, b, c, d, e, f):
        self.name = a
        self.surname = b
        self.age = c
        self.height = d
        self.colorhair = e
        self.coloreye = f
    def getinfo(self):
        print(self.name)
        print(self.surname)
        print(self.age)
        print(self.height)
        print(self.colorhair)
        print(self.coloreye)
me = human(input(), input(), input(), input(), input(), input())
human.getinfo(me)