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
from sympy import symbols

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
def calculate_convergence_rates(y_euler, y_euler_back, y_crank_nicolson):
    rates = []

    # Calculate convergence rates
    for i in range(1, len(y_euler)):
        rate_euler = y_euler[i] / y_euler[i - 1]
        rate_euler_back = y_euler_back[i] / y_euler_back[i - 1]
        rate_crank_nicolson = y_crank_nicolson[i] / y_crank_nicolson[i - 1]

        rates.append((rate_euler, rate_euler_back, rate_crank_nicolson))

    return rates

def ex2():
    x = sym.symbols('x')
    y0 = 0.1
    T = 1
    N_values = [2, 4, 8, 12, 16]  # Different values of N (step sizes)
    dy = x - x ** 3

    convergence_rates = {'Euler': [], 'Euler Backwards': [], 'Crank Nicolson': []}

    for N in N_values:
        de_exact = DeExactResult(y0, T, N)
        y_exact = de_exact.calculate()

        euler = EulerMethod(y0, T, N, dy)
        y_euler = euler.calculate()

        euler_back = EulerBackwardMethod(y0, T, N, dy)
        y_euler_back = euler_back.calculate()

        crank_nicolson = CrankNicolsonMethod(y0, T, N, dy)
        y_crank_nicolson = crank_nicolson.calculate()

        # Calculate and store convergence rates
        rates = calculate_convergence_rates(y_euler, y_euler_back, y_crank_nicolson)
        convergence_rates['Euler'].append(rates[0][0])
        convergence_rates['Euler Backwards'].append(rates[0][1])
        convergence_rates['Crank Nicolson'].append(rates[0][2])


    for method, rates in convergence_rates.items():
        plt.loglog(N_values, rates, marker='o', label=method)

    plt.xlabel('Number of Steps (N)')
    plt.ylabel('Convergence Rate')
    plt.legend()
    plt.show()

ex2()

x = symbols('x')
y0 = 0.1
T = 1
N = 6
dy = x - x**3
def error_rate_func(y0, T, N, dy, acc, method):
    error = []
    ratio = []
    idx = 0
    N = 1
    while True:
        de_exact = DeExactResult(y0, T, N).calculate()
        y_exact = de_exact
        euler_method = method(y0, T, N, dy).calculate()
        y_method = euler_method
        error.append((np.abs(y_exact - y_method).sum() / len(y_method)))

        if idx > 0:
            rate = np.log2(error[idx - 1] / error[idx])
            ratio.append(rate)
            if idx > 1:
                if (np.abs(ratio[idx - 1] - ratio[idx - 2]) < acc) and ((round(ratio[idx - 1]) - ratio[idx - 1]) < acc):
                    break
        idx += 1
        N *= 2
    return error, ratio



def error_ratio_exercise2(y0, T, dy, acc):
    error_euler = []
    error_euler_b = []
    error_crank_n = []
    rate_euler = []
    rate_euler_b = []
    rate_crank_n = []

    error_euler, rate_euler = error_rate_func(y0, T, N, dy, acc, EulerMethod)
    error_euler_b, rate_euler_b = error_rate_func(y0, T, N, dy, acc, EulerMethod)
    error_crank_n, rate_crank_n = error_rate_func(y0, T, N, dy, acc, CrankNicolsonMethod)

    return (error_euler, error_euler_b, error_crank_n, rate_euler, rate_euler_b, rate_crank_n)


#Parameters
acc = 0.01
y0 = 0.1
T = 1

#Compute errors and rate
error_euler, error_euler_b, error_crank_n, rate_euler, rate_euler_b, rate_crank_n = error_ratio_exercise2(y0, T, dy, acc)
error_euler_df = pd.DataFrame(error_euler, columns = ['Error Euler'])
error_euler_b_df= pd.DataFrame(error_euler_b, columns = ['Error Euler B.'])
error_crank_n_df = pd.DataFrame(error_crank_n, columns = ['Error Crank N.'])
results_df = pd.concat([error_euler_df, error_euler_b_df, error_crank_n_df], axis = 1)
results_df.index +=1


print("2)\n")
print(f'\t\tRate Euler\t{rate_euler[-1]}')
print(f'\t\tRate Euler Backwards\t{rate_euler_b[-1]}')
print(f'\t\tRate Crack Nicolson\t{rate_crank_n[-1]}')