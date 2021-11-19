from abstractclasses import solver, solver_model

"""
Numberset solver is extremely complex and still unstable
"""


class number_set_solver(solver):
    def prompt_inputs(self) -> None:
        operation_types = ["Contains", "Divisible By", "Ends With"]
        operation = self.prompt_choices(
            "Please choose which operation you would like to perform.",
            operation_types,
        )
        lower_bound = self.prompt_integer(
            "Please enter the lower value in the set > "
        )
        upper_bound = self.prompt_integer(
            "Please enter the higher value in the set > ", lower_bound
        )
        val_amt = self.prompt_integer(
            "Please enter the amount of values that we will be working "
            + "with > ",
            1,
        )

        # Set inputs
        self.inputs["lower-bound"] = lower_bound
        self.inputs["upper_bound"] = upper_bound
        self.inputs["val_amt"] = val_amt
        self.inputs["operation"] = operation


class number_set_model(solver_model):
    def solve(self) -> None:
        return super().solve()
