import math
import numpy as np
from Methods.BackwardEulerMethod import BackwardEulerMethod
from Methods.CrankNicolsonMethod import CrankNicolsonMethod
from Methods.EulerMethod import EulerMethod
from Rules.MidPointRule import MidPointRule
from Rules.NewtonSolver import NewtonSolver
from Rules.TrapezoidalRule import TrapezoidalRule
from Rules.SimpsonRule import SimpsonsRule
from Rules.NumericalIntegrationAnalyzer import NumericalIntegrationAnalyzer
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
def f(y):
    return y - y**3


y0 = 2.0
T = 5.0
N = 1000
solver = NewtonSolver()  # Create a solver for nonlinear algebraic equations

euler_solver = EulerMethod(y0, T, N)
t_euler, y_euler = euler_solver.solve()

backward_euler_solver = BackwardEulerMethod(y0, T, N, solver)
t_backward_euler, y_backward_euler = backward_euler_solver.solve()

crank_nicolson_solver = CrankNicolsonMethod(y0, T, N, solver)
t_crank_nicolson, y_crank_nicolson = crank_nicolson_solver.solve()


# Solve using the Euler method
t_euler, y_euler = euler_solver.solve()

# Solve using the Backward Euler method
t_backward_euler, y_backward_euler = backward_euler_solver.solve()

# Solve using the Crank-Nicolson method
t_crank_nicolson, y_crank_nicolson = crank_nicolson_solver.solve()

def f(y):
    return y - y**3


y0 = 0.1
T = 5.0
N = 8
print("Start")
solver = NewtonSolver()  # Create a solver for nonlinear algebraic equations

# Example usage for Euler method
euler_solver = EulerMethod(y0, T, N)
t_euler, y_euler = euler_solver.solve()
print("t_euler:\t" ,t_euler, y_euler)


# Example usage for Backward Euler method
backward_euler_solver = BackwardEulerMethod(y0, T, N, solver)
t_backward_euler, y_backward_euler = backward_euler_solver.solve()
print("t_backward_euler:\t" ,t_backward_euler, y_backward_euler)

# Example usage for Crank-Nicolson method
crank_nicolson_solver = CrankNicolsonMethod(y0, T, N, solver)
t_crank_nicolson, y_crank_nicolson = crank_nicolson_solver.solve()
print("t_crank_niclson:\t" ,t_crank_nicolson, y_crank_nicolson)
