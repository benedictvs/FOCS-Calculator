from abstractclasses import solver, solver_model

"""
Here is a good example of how simple it can be to add modules. Unfortunately,
the solving functions are a little sloppy, and could use some further
revision.
Roman Numeral module takes a valid Roman numeral and translates it to base 10
"""

# ————————————————————————————————————————————————
# MODULAR ARITHMETIC SOLVER CLASS
# ————————————————————————————————————————————————


class modular_arithmetic_solver(solver):
    def prompt_inputs(self) -> None:

        base = self.prompt_integer("Please enter the base > ")
        exponent = self.prompt_integer("Please enter the exponent > ")
        mod = self.prompt_integer("Please enter the mod > ")

        self.inputs["base"] = base
        self.inputs["exponent"] = exponent
        self.inputs["mod"] = mod


# ————————————————————————————————————————————————
# MODULAR ARITHMETIC MODEL CLASS
# ————————————————————————————————————————————————


class modular_arithmetic_model(solver_model):
    def solve(self) -> None:
        base = self.inputs["base"]
        exponent = self.inputs["exponent"]
        mod = self.inputs["mod"]
        self.ans = self.modular(base, exponent, mod)
        self.work = self.modularwork(base, exponent, mod)

    def modular(self, base: int, exponent: int, mod: int) -> int:
        binexp = bin(exponent).replace("0b", "")
        powlist = list(binexp)
        for i in range(0, len(powlist)):
            powlist[i] = int(powlist[i])

        currentmod = 1
        for i in range(0, len(powlist)):
            multmod = (currentmod ** 2) * (2 ** powlist[i])
            newmod = multmod % mod
            currentmod = newmod
        return multmod % mod

    def modularwork(self, base: int, exponent: int, mod: int) -> str:
        binexp = bin(exponent).replace("0b", "")
        powlist = list(binexp)
        for i in range(0, len(powlist)):
            powlist[i] = int(powlist[i])
        calculations = []
        currentmod = 1
        for i in range(0, len(powlist)):
            c = i + 1
            multmod = (currentmod ** 2) * (2 ** powlist[i])
            newmod = multmod % mod
            mathstr = "c({}) ≡ {}^2 * 2^{} = {} * {} = {}mod{} = {}".format(
                c,
                currentmod,
                powlist[i],
                currentmod ** 2,
                2 ** powlist[i],
                multmod,
                mod,
                newmod,
            )
            currentmod = newmod
            calculations.append(mathstr)

        v = "Convert {} to binary: {}\n".format(exponent, binexp)
        for i in range(0, len(calculations)):
            v += "{}\t|\t{}".format(powlist[i], calculations[i]) + "\n"
        v += "You are left with remainder {}".format(multmod % mod)
        return v
