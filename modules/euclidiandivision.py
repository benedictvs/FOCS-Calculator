from abstractclasses import solver, solver_model

"""
The Euclidian Division module performs Euclidian division (division with
remainder) recursively until it finds a greatest common divisor.
"""

# ————————————————————————————————————————————————
# EUCLIDIAN DIVISION SOLVER CLASS
# ————————————————————————————————————————————————


class euclidian_division_solver(solver):
    def prompt_inputs(self) -> None:
        x_arg = self.prompt_integer("Please enter the dividend > ")
        y_arg = self.prompt_integer("Please enter the divisor > ", x_arg)

        # Set inputs
        self.inputs["x_arg"] = x_arg
        self.inputs["y_arg"] = y_arg


# ————————————————————————————————————————————————
# EUCLIDIAN DIVISION MODEL CLASS
# ————————————————————————————————————————————————


class euclidian_division_model(solver_model):
    def solve(self) -> None:
        x = self.inputs["x_arg"]
        y = self.inputs["y_arg"]

        self.ans = self.euclid(x, y)
        self.work = self.euclidwork(x, y, "")

    def euclid(self, x: int, y: int) -> int:
        """
        Recursive function, returns integer answer when done
        """
        if y == 0:
            return x
        else:
            return self.euclid(y, x % y)

    def euclidwork(self, x: int, y: int, v: str) -> str:
        """
        Recursive function, returns string of work when done
        """
        if y == 0:
            v += "Final GCD is {}".format(x)
            return v
        else:
            if x > y and x % y != 0:
                v += (
                    "{} goes into {} {} times, with a remainder of {}.".format(
                        y, x, x // y, x % y
                    )
                    + " Now perform gcd({}, {})".format(x % y, y)
                    + "\n"
                )
            elif x > y and x % y == 0:
                v += (
                    "{} goes into {} {} times, with a remainder of {}.".format(
                        y, x, x // y, x % y
                    )
                    + " We have arrived at our GCD."
                    + "\n"
                )
            return self.euclidwork(y, x % y, v)
