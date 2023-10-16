class EulerMethod:
    def __init__(self, y0, T, N):
        self.y0 = y0
        self.T = T
        self.N = N
        self.h = T / N

    def solve(self):
        t_values = [i * self.h for i in range(self.N + 1)]
        y_values = [self.y0]

        for i in range(self.N):
            y_next = y_values[-1] + self.h * (y_values[-1] - y_values[-1]**3)
            y_values.append(y_next)

        return t_values, y_values
