import numpy as np
import matplotlib.pyplot as plt
from Rules.MidPointRule import MidPointRule
from Rules.TrapezoidalRule import TrapezoidalRule
from Rules.SimpsonRule import SimpsonsRule

class NumericalIntegrationAnalyzer:
    def __init__(self, func, left, right, len_of_results, ground_truth=1.0):
        self.func = func
        self.left = left
        self.right = right
        self.len_of_results = len_of_results
        self.ground_truth = ground_truth

        self.results_midpoint = np.array([self.run_method(MidPointRule, 2**i) for i in np.arange(1, len_of_results)])
        self.results_trapezoid = np.array([self.run_method(TrapezoidalRule, 2**i) for i in np.arange(1, len_of_results)])
        self.results_simpsons = np.array([self.run_method(SimpsonsRule, 2**i) for i in np.arange(1, len_of_results)])

        self.errors_midpoint = self.err(self.ground_truth, self.results_midpoint)
        self.errors_trapezoid = self.err(self.ground_truth, self.results_trapezoid)
        self.errors_simpsons = self.err(self.ground_truth, self.results_simpsons)

        self.x = 2**np.arange(2, self.len_of_results)

        print("1-b)\n")
        self.convergence_rate_midpoint = self.convergence_ratee(self.errors_midpoint)
        print(f'\t\tConvergence\t{self.convergence_rate_midpoint[0]}')
        self.convergence_rate_trapezoid = self.convergence_ratee(self.errors_trapezoid)
        print(f'\t\tConvergence\t{self.convergence_rate_trapezoid[0]}')
        self.convergence_rate_simpsons = self.convergence_ratee(self.errors_simpsons)
        print(f'\t\tConvergence\t{self.convergence_rate_simpsons[0]}')

    def run_method(self, method_class, n):
        method = method_class(self.func, self.left, self.right, n)
        return method.evaluate()

    @staticmethod
    def err(ground_truth, estimate):
        return np.abs(ground_truth - estimate)

    @staticmethod
    def convergence_rate(err1, err2):
        return np.log2(err1 / err2)

    def convergence_ratee(self, errors):
        return np.array([self.convergence_rate(errors[i], errors[i + 1]) for i in range(len(errors) - 1)])

    def plot_convergence_rates(self):
        plt.loglog(self.x, self.convergence_rate_midpoint, label="Composite Midpoint")
        plt.loglog(self.x, self.convergence_rate_trapezoid, label="Composite Trapezoidal")
        plt.loglog(self.x, self.convergence_rate_simpsons, label="Composite Simpsons")
        plt.legend()
        plt.show()
