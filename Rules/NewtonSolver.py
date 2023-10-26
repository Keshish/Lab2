import sympy as sym

class NewtonMethod:
    def __init__(self, f, df, sp, precision):
        self.f = f
        self.df = df
        self.sp = sp
        self.precision = precision
        self.x = sym.symbols('x')  # Define 'x' as a symbolic variable

    def solve(self):
        iterations = 0

        while abs(self.f.subs(self.x, self.sp).evalf()) > self.precision:
            if self.df.subs(self.x, self.sp).evalf() == 0:
                print("zero error")
                break

            self.sp = self.sp - (self.f.subs(self.x, self.sp) / self.df.subs(self.x, self.sp)).evalf()
            iterations += 1


        return self.sp, iterations
