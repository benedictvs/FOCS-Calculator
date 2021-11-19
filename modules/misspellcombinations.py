from abstractclasses import solver, solver_model

"""
Misspell combinations solves for how many ways one can misspell a word
"""

# ————————————————————————————————————————————————
# MISSPELL COMBINATIONS SOLVER CLASS
# ————————————————————————————————————————————————


class misspell_combinations_solver(solver):
    def prompt_inputs(self) -> None:
        n_arg = self.prompt_string(
            "How many ways can you misspell the word: (Enter word)"
        )
        k_arg = self.prompt_integer(
            "Length of the word you want to misspell: ", lower_bound=1
        )

        # Set inputs
        self.inputs["n_arg"] = n_arg
        self.inputs["k_arg"] = k_arg
        self.inputs["MAX_CHAR"] = 26


# ————————————————————————————————————————————————
# MISSPELL COMBINATIONS MODEL CLASS
# ————————————————————————————————————————————————


class mispell_combinations_model(solver_model):
    def __init__(self, **inputs) -> None:
        super().__init__(**inputs)
        self.MAX_CHAR = self.inputs["MAX_CHAR"]

    def solve(self) -> None:
        n = self.inputs["n_arg"]
        k = self.inputs["k_arg"]

        self.ans = str(self.misspell(n, k))
        self.work = self.misspellwork(n, k)

    def factorial(self, j: int) -> int:
        """
        Utility function to find factorial of n
        """
        fact = 1
        for i in range(2, j + 1):
            fact = fact * i
        return fact

    def misspell(self, n: str, k: int) -> int:
        """
        Finds the maximum possible misspell combinations
        """
        length = len(n)
        freq = [0] * self.MAX_CHAR

        # finding frequency of all the lower
        # case alphabet and storing them in
        # array of integer
        for i in range(0, length):
            if n[i] >= "a":
                freq[(ord)(n[i]) - 97] = freq[(ord)(n[i]) - 97] + 1

        # finding factorial of number of
        # appearances and multiplying them
        # since they are repeating alphabets
        fact = 1
        for i in range(0, self.MAX_CHAR):
            fact = fact * self.factorial(freq[i])

        # finding factorial of size of string
        # and dividing it by factorial found
        # after multiplying
        return self.factorial(length) / fact

    def misspellwork(self, n: str, k: int) -> str:
        """
        Shows the work necessary to find the maximum mispell combinations.
        """
        steps = "Recall the Permutations equation:\n"
        steps += "n! / (n-k)!\n"
        steps += "Plug in our value for n (length of the word):\n"
        steps += "{}! / ({}-k)!\n".format(len(n), len(n))
        steps += (
            "Finally, plug in our value for k the number of letters we want "
            + "to choose and compute:\n"
        )
        steps += "{}! / (({}-{})!)\n".format(len(n), len(n), k)
        steps += "={} \n".format(self.misspell(n, k))
        return steps
