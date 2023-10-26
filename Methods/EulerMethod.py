import numpy as np
import sympy as sym  # Add this import

class EulerMethod:
    def __init__(self, y0, T, N, dy):
        self.y0 = y0
        self.T = T
        self.N = N
        self.dy = dy
        self.h = T / N

    def calculate(self):
        x = sym.symbols('x')  # Define 'x' as a symbolic variable
        y = np.zeros(self.N + 1)
        y[0] = self.y0
        for n in range(self.N):
            y[n + 1] = y[n] + self.h * float(self.dy.subs(x, y[n]))
        return y
