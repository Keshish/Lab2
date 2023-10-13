import math
from Rules.MidPointRule import MidPointRule
from Rules.TrapezoidalRule import TrapezoidalRule
from Rules.SimpsonRule import SimpsonsRule
from Rules.ConvergenceAnalysis import ConvergenceAnalysis
import matplotlib.pyplot as plt

# Test the quadrature rules on ∫[0, π/2] sin(x) dx, known to be 1
exact_value = 1
a = 0
b = math.pi / 2

sin_func = lambda x: math.sin(x)

midpoint_rule = MidPointRule(sin_func, a, b, n=10)
trapezoidal_rule = TrapezoidalRule(sin_func, a, b, n=10)
simpsons_rule = SimpsonsRule(sin_func, a, b, n=10)


print(midpoint_rule.evaluate())
print(trapezoidal_rule.evaluate())
print(simpsons_rule.evaluate())

# Define the integration interval
a = 0
b = math.pi / 2  # π/2

# Initialize lists to store errors and h values
max_num_subintervals = 8
midpoint_analysis = ConvergenceAnalysis(MidPointRule, sin_func, a, b)
trapezoidal_analysis = ConvergenceAnalysis(TrapezoidalRule, sin_func, a, b)
simpsons_analysis = ConvergenceAnalysis(SimpsonsRule, sin_func, a, b)

# Perform convergence analysis
midpoint_analysis.compute_errors_and_convergence_rates(max_num_subintervals)
trapezoidal_analysis.compute_errors_and_convergence_rates(max_num_subintervals)
simpsons_analysis.compute_errors_and_convergence_rates(max_num_subintervals)


# Estimate convergence rates
midpoint_rates = midpoint_analysis.estimate_convergence_rate()
trapezoidal_rates = trapezoidal_analysis.estimate_convergence_rate()
simpsons_rates = simpsons_analysis.estimate_convergence_rate()

# Limit the number of displayed convergence rates
max_displayed_rates = 100  # You can adjust this as needed

# Print the limited number of convergence rates
print(f'Estimated Convergence Rate (Midpoint Rule): {midpoint_rates[:max_displayed_rates]}')
print(f'Estimated Convergence Rate (Trapezoidal Rule): {trapezoidal_rates[:max_displayed_rates]}')
print(f'Estimated Convergence Rate (Simpson\'s Rule): {simpsons_rates[:max_displayed_rates]}')

# Plot the log-log graph
plt.figure(figsize=(10, 6))
plt.loglog(midpoint_analysis.hs, midpoint_analysis.errors, 'o-', label='Midpoint Rule', markersize=8)
plt.loglog(trapezoidal_analysis.hs, trapezoidal_analysis.errors, 's-', label='Trapezoidal Rule', markersize=8)
plt.loglog(simpsons_analysis.hs, simpsons_analysis.errors, '^-', label="Simpson's Rule", markersize=8)
plt.xlabel('h', fontsize=14)
plt.ylabel('Error', fontsize=14)
plt.title('Convergence Rates of Quadrature Methods', fontsize=16)
plt.legend()
plt.grid()
plt.show()


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
# In other words, the accuracy of the composite trapezoidal rule with equal weights
# will not improve as rapidly with smaller subintervals as it would with the original
# rule that has unequal weights. This is because the original trapezoidal rule accounts
# for the shape of the function by using the appropriate weights, whereas equal
# weights do not capture the function's behavior as effectively.