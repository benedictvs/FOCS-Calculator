from pylambdac import parse

from abstractclasses import solver, solver_model


class lambda_calculus_solver(solver):
    def prompt_inputs(self) -> None:
        expr = self.prompt_string("Enter a lambda calculus expression")

        self.inputs['expr'] = expr


class lambda_calculus_model(solver_model):
    def solve(self) -> None:
        expr = self.inputs['expr']
        work = self.parse_lambda_expr(expr)
        self.ans = str(work[-1])
        self.work = str(work)

    def parse_lambda_expr(self, expr):
        new = []
        state = parse.parse_expr(expr)
        while state is not None:
            new.append(str(state))
            state = state.reduce_once({})
        return new
