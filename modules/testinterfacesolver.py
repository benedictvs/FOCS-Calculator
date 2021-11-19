from questionary import print

from abstractclasses import solver, solver_model


class test_solver(solver):
    def prompt_inputs(self) -> None:
        print(self.name)
        self.inputs = self.prompt_integer("Get Val", lower_bound=0)

    def print_outputs(self) -> None:
        print(self.ans)
        print(self.work)


class test_solver_model(solver_model):
    def solve(self) -> None:
        self.ans = "1"
        self.work = "2"
