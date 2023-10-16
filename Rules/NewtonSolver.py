class NewtonSolver:
    def solve(self, h, t, y_n, f_n, max_iterations=100, tolerance=1e-6):
        # Newton-Raphson method to solve for the next y
        iteration = 0

        while iteration < max_iterations:
            # Compute the function value and its derivative
            f = y_n - y_n**3
            df = 1 - 3 * y_n**2

            # Update the estimate for the root
            y_next = y_n - f / df

            # Check for convergence
            if abs(y_next - y_n) < tolerance:
                return y_next

            y_n = y_next
            iteration += 1

        # Return the computed y_next (even if it didn't converge)
        return y_next
