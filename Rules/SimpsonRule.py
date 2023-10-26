
class SimpsonsRule:
    def __init__(self, func, a, b, n):
        self.func = func
        self.a = a
        self.b = b
        self.n = n
        self.h = (b - a) / n

    def evaluate(self):
        result = self.func(self.a) + self.func(self.b)
        for i in range(1, self.n):
            xi = self.a + i * self.h
            if i % 2 == 0:
                result += 2 * self.func(xi)
            else:
                result += 4 * self.func(xi)
        result *= self.h / 3
        return result