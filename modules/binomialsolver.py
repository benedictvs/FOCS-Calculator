import math as m

from questionary import prompt, print

from abstractclasses import solver, solver_model

"""
Binomial Coefficient module solves for the number of combinations of k
elements in a set of n elements. 
"""

# ————————————————————————————————————————————————
# BINOMIAL COEFFICIENT SOLVER CLASS
# ————————————————————————————————————————————————


class binomial_coefficient_solver(solver):
    def prompt_inputs(self) -> None:
        n_arg = self.prompt_integer(
            "Please enter the size of the set of elements (n) > ", 1)
        k_arg = self.prompt_integer(
            "Please enter how many elements are chosen from that set (k) > ",
            1, n_arg)

        # Set inputs
        self.inputs['n_arg'] = n_arg
        self.inputs['k_arg'] = k_arg

# ————————————————————————————————————————————————
# BINOMIAL COEFFICIENT MODEL CLASS
# ————————————————————————————————————————————————


class binomial_coefficient_model(solver_model):
    def solve(self) -> None:
        """
        Takes self.inputs and solves the binomial coefficient
        """
        n = self.inputs['n_arg']
        k = self.inputs['k_arg']
        self.ans = self.binomial(n, k)
        self.work = self.binomialwork(n, k)

    def binomial(self, n: int, k: int) -> int:
        """
        Binomial coefficient formula
        """
        return m.factorial(n) / (m.factorial(k) * (m.factorial(n-k)))

    def binomialwork(self, n: int, k: int) -> str:
        steps = 'Recall the binomial coefficient equation:\n'
        steps += 'n! / (k! * (n-k!))\n'
        steps += 'Plug in our value for n:\n'
        steps += '{}! / (k! * ({}-k)!)\n'.format(n, n)
        steps += 'Finally, plug in our value for k and compute:\n'
        steps += '{}! / ({}! * ({}-{})!)\n'.format(n, k, n, k)
        steps += '={}'.format(self.binomial(n, k))
        return steps
