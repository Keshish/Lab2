from Methods.BackwardEulerMethod import EulerBackwardMethod
from Methods.CrankNicolsonMethod import CrankNicolsonMethod
from Methods.EulerMethod import EulerMethod
from Rules.MidPointRule import MidPointRule
from Rules.TrapezoidalRule import TrapezoidalRule
from Rules.SimpsonRule import SimpsonsRule
from Rules.NumericalIntegrationAnalyzer import NumericalIntegrationAnalyzer
from Methods.DeExactResult import DeExactResult
import numpy as np
import sympy as sym
import math
import pandas as pd
import matplotlib.pyplot as plt


exact_value = 1
a = 0
b = math.pi / 2

sin_func = lambda x: math.sin(x)

midpoint_rule = MidPointRule(sin_func, a, b, n=10)
trapezoidal_rule = TrapezoidalRule(sin_func, a, b, n=10)
simpsons_rule = SimpsonsRule(sin_func, a, b, n=10)

print("1-a)\n")
print(f'\t\tMidpoint\t{midpoint_rule.evaluate()}')
print(f'\t\tTrapezoidal {trapezoidal_rule.evaluate()}')
print(f'\t\tSimpsons\t{simpsons_rule.evaluate()}\n')



func = np.sin
aa = np.pi / 2
bb = 0
nn = 10

analyzer = NumericalIntegrationAnalyzer(func, bb, aa, nn)
analyzer.plot_convergence_rates()


#####
#C
# If you make a mistake when implementing the composite trapezoidal rule
# by neglecting the half-valued weights at the endpoints and
# set all the weights equal (wi = h for i = 1, ..., N + 1), the convergence rate will change.
# The original composite trapezoidal rule with unequal weights provides an estimate
# of the integral that has a convergence rate of O(h^2), where "h" is the size of each subinterval.
# This means that as you reduce the subinterval size (increase N), the error decreases quadratically.
# However, if you use equal weights (wi = h for all i), the convergence rate will be reduced to O(h),
# which means that the error decreases linearly as the subinterval size decreases.
# The accuracy of the composite trapezoidal rule with equal weights
# will not improve as rapidly with smaller subintervals as it would with the original
# rule that has unequal weights. This is because the original trapezoidal rule accounts
# for the shape of the function by using the appropriate weights, whereas equal
# weights do not capture the function's behavior as effectively.


#Exercise 2
#a
def ex2():
    x = sym.symbols('x')
    y0 = 0.1
    T = 1
    N = 6
    dy = x - x**3

    de_exact = DeExactResult(y0, T, N)
    y_exact = de_exact.calculate()

    euler = EulerMethod(y0, T, N, dy)
    y_euler = euler.calculate()

    euler_back = EulerBackwardMethod(y0, T, N, dy)
    y_euler_back = euler_back.calculate()

    crank_nicolson = CrankNicolsonMethod(y0, T, N, dy)
    y_crank_nicolson = crank_nicolson.calculate()

    # Plots of the approximations and the exact solution
    plt.figure()
    x_lin = np.linspace(0, T, N + 1)
    plt.plot(x_lin, y_exact)
    plt.plot(x_lin, y_euler)
    plt.plot(x_lin, y_euler_back)
    plt.plot(x_lin, y_crank_nicolson)
    plt.legend(['Exact solution', 'Euler Solution', 'Euler Backwards Solution', 'Crank Nicolson Solution'])
    plt.show()

    print("2)\n")
    print(f'\t\tRate Euler\t{y_euler[-1]}')
    print(f'\t\tRate Euler Backwards\t{y_euler_back[-1]}')
    print(f'\t\tRate Crack Nicolson\t{y_crank_nicolson[-1]}')


ex2()