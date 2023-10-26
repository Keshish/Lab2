import numpy as np
import sympy as sym
from Rules.NewtonSolver import NewtonMethod

class EulerBackwardMethod:
    def __init__(self, y0, T, N, dy):
        self.y0 = y0
        self.T = T
        self.N = N
        self.dy = dy
        self.h = T / N

    def calculate(self):
        x = sym.symbols('x')
        y = np.zeros(self.N + 1)
        y[0] = self.y0
        for n in range(self.N):
            fN = x - y[n] - self.h * self.dy
            newton = NewtonMethod(fN, sym.diff(fN, x), y[n], 10**(-4))
            root, _ = newton.solve()  # Extract the root value and ignore the number of iterations
            y[n + 1] = root  # Store the root value in the y array
        return y
