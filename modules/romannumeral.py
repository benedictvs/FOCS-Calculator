from abstractclasses import solver, solver_model

"""
Here is a good example of how simple it can be to add modules. Unfortunately,
the solving functions are a little sloppy, and could use some further
revision.

Roman Numeral module takes a valid Roman numeral and translates it to base 10
"""

# ————————————————————————————————————————————————
# ROMAN NUMERAL SOLVER CLASS
# ————————————————————————————————————————————————


class roman_numeral_solver(solver):
    def prompt_inputs(self) -> None:
        def validate(val: str, *args) -> bool:
            """
            Helper function validates whether the user's value in a set
            """
            myset = args[0][0]
            for i in range(0, len(val)):
                if not val[i] in myset:
                    return False
            return True

        valid_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        exp = self.prompt_string(
            "Please enter the Roman numeral expression > ",
            validate,
            valid_numerals,
        )

        self.inputs["exp"] = exp
        self.inputs["valid_numerals"] = valid_numerals


# ————————————————————————————————————————————————
# ROMAN NUMERAL MODEL CLASS
# ————————————————————————————————————————————————


class roman_numeral_model(solver_model):
    def solve(self) -> None:
        expression = self.inputs["exp"]
        self.ans = self.roman(expression)
        self.work = self.romanwork(expression)

    def roman(self, expression: str) -> int:
        """
        Takes a Roman Numeral expression and solves for a base 10 integer
        """
        nums = self.inputs["valid_numerals"]

        romalist = list(expression)
        if len(romalist) == 1:
            return nums[expression]
        sums = []
        for i in range(0, len(romalist) - 1):
            if nums[romalist[i]] < nums[romalist[i + 1]]:
                sums.append(nums[romalist[i]] * -1)
            else:
                sums.append(nums[romalist[i]])
        sums.append(nums[romalist[-1]])
        return sum(sums)

    def romanwork(self, expression: str) -> str:
        """
        Takes Roman numeral expression, then shows the work to solve for
        base 10 int
        """
        nums = self.inputs["valid_numerals"]

        romalist = list(expression)
        unique_romalist = set(romalist)
        unique_romalist = list(unique_romalist)
        recallstr = "Recall that: "
        for i in range(0, len(unique_romalist) - 1):
            recallstr += (
                unique_romalist[i]
                + " = "
                + str(nums[unique_romalist[i]])
                + ", "
            )
        recallstr += (
            "and "
            + unique_romalist[-1]
            + " = "
            + str(nums[unique_romalist[-1]])
        )
        if len(romalist) == 1:
            return nums[expression]
        sums = []
        formula = ""
        simpleformula = ""
        for i in range(0, len(romalist) - 1):
            if nums[romalist[i]] < nums[romalist[i + 1]]:
                sums.append(nums[romalist[i]] * -1)
                formula += (
                    " "
                    + romalist[i]
                    + "("
                    + str(nums[romalist[i]] * -1)
                    + ") +"
                )
                simpleformula += " " + str(nums[romalist[i]] * -1) + " +"
            else:
                sums.append(nums[romalist[i]])
                formula += (
                    " " + romalist[i] + "(" + str(nums[romalist[i]]) + ") +"
                )
                simpleformula += " " + str(nums[romalist[i]]) + " +"
        formula += " " + romalist[-1] + "(" + str(nums[romalist[-1]]) + ")"
        simpleformula += " " + str(nums[romalist[-1]])
        sums.append(nums[romalist[-1]])
        val = sum(sums)
        return (
            recallstr
            + "\n"
            + formula
            + "\n"
            + simpleformula
            + "\n"
            + "= {}".format(val)
        )
