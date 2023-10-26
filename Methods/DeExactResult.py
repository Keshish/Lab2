import numpy as np
import math

class DeExactResult:
    def __init__(self, y0, T, N):
        self.y0 = y0
        self.T = T
        self.N = N
        self.h = T / N

    def calculate(self):
        y = np.zeros(self.N + 1)
        y[0] = self.y0
        for n in range(self.N):
            y[n + 1] = self.y0 / (np.sqrt(self.y0**2 - (self.y0**2 - 1) * math.e**(-2 * self.h * n)))
        return y
