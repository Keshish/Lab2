
class TrapezoidalRule:
    def __init__(self, func, a, b, n):
        self.func = func
        self.a = a
        self.b = b
        self.n = n
        self.h = (b - a) / n

    def evaluate(self):
        result = (self.func(self.a) + self.func(self.b)) / 2
        for i in range(1, self.n):
            xi = self.a + i * self.h
            result += self.func(xi)
        result *= self.h
        return result