from questionary import print
from solverinterfacesfc import solver, solver_model


class test_solver(solver):
    def prompt_inputs(self) -> None:
        self.inputs = self.prompt_integer("Test")

    def print_outputs(self) -> None:
        print(self.ans)
        print(self.work)


class test_solver_model(solver_model):
    def solve(self):
        self.ans = "1"
        self.work = "2"
