import math

class MidPointRule:
    def __init__(self, func, a, b, n):
        self.func = func
        self.a = a
        self.b = b
        self.n = n
        self.h = (b - a) / n

    def evaluate(self):
        result = 0
        for i in range(self.n):
            xi = self.a + i * self.h + self.h / 2
            result += self.func(xi)
        result *= self.h
        return result
