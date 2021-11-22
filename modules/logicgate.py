from abstractclasses import solver, solver_model

"""
Logic Gate module implement several kinds of logic gates, takes inputs
and shows work
"""


class logic_gate_solver(solver):
    def prompt_inputs(self) -> None:
        a_arg = self.prompt_integer(
            "Please enter 0 or 1 for the value of A > ", 0, 1
        )
        b_arg = self.prompt_integer(
            "Please enter 0 or 1 for value of B > ", 0, 1
        )
        choices = ["not_gate", "and_gate", "or_gates", "xor_gate"]
        e_arg = self.prompt_choices(
            "Please specify not_gate, and_gate, or_gate, or xor_gate", choices
        )

        # Set inputs
        self.inputs["a_arg"] = a_arg
        self.inputs["b_arg"] = b_arg
        self.inputs["e_arg"] = e_arg


class logic_gate_model(solver_model):
    def solve(self) -> None:
        """
        Takes self.inputs and puts them into the not_gate, or_gate and and_gate
        """
        a = self.inputs["a_arg"]
        b = self.inputs["b_arg"]
        e = self.inputs["e_arg"]
        self.ans = str(self.logic(a, b, e))
        self.work = self.logicwork(a, b, e)

    # Function Calls
    def logic(self, a: int, b: int, e: str) -> int:
        if e == "not_gate":
            if a:
                return 0
            else:
                return 1
        if e == "or_gate":
            # TODO: implement logical OR
            if a:
                return 1
            if b:
                return 1
            else:
                return 0
        if e == "and_gate":
            # TODO: implement logical AND
            if a:
                if b:
                    return 1
            else:
                return 0
        if e == "xor_gate":
            # TODO: implement logical XOR
            if a ^ b:
                return 1
            else:
                return 0

    def logicwork(self, a: int, b: int, e: str) -> str:
        if e == "not_gate":
            steps = (
                "Recall that the not gate takes whatever bit a represents "
                + "and returns the opposite:\n"
            )
            steps += "taking our value for a: \n"
            steps += "not {} = {}\n".format(a, self.logic(a, b, e))
            return steps
        if e == "or_gate":
            steps = (
                "Recall that the or gate returns TRUE if either a or b is"
                + " TRUE:\n"
            )
            steps += "taking our values for a and b: \n"
            steps += "{} or {} = {}\n".format(a, b, self.logic(a, b, e))
            return steps
        if e == "and_gate":
            steps = (
                "Recall that the and gate returns TRUE only if a and b is"
                + " TRUE:\n"
            )
            steps += "taking our values for a and b: \n"
            steps += "{} or {} = {}\n".format(a, b, self.logic(a, b, e))
            return steps
        if e == "xor_gate":
            steps = (
                "Recall that the exlusive or gate returns TRUE only if "
                + "either a or b is TRUE:\n"
            )
            steps += "taking our values for a and b: \n"
            steps += "{} or {} = {}\n".format(a, b, self.logic(a, b, e))
            return steps
