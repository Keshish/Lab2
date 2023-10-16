class CrankNicolsonMethod:
    def __init__(self, y0, T, N, solver):
        self.y0 = y0
        self.T = T
        self.N = N
        self.h = T / N
        self.solver = solver

    def solve(self):
        t_values = [i * self.h for i in range(self.N + 1)]
        y_values = [self.y0]

        for i in range(self.N):
            t = t_values[i]
            y_n = y_values[-1]
            f_n = y_n - y_n**3

            # Calculate the next y using the Crank-Nicolson method
            y_next = self.solver.solve(self.h, t, y_n, f_n)
            y_values.append(y_next)

        return t_values, y_values
