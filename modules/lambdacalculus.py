from pylambdac import parse

from abstractclasses import solver, solver_model

"""
lambdacalculus takes a lambda calculus expression and reduces it to weak head
normal form
"""

# ————————————————————————————————————————————————
# LAMBDA CALCULUS MODEL CLASS
# ————————————————————————————————————————————————


class lambda_calculus_solver(solver):
    def convert_lambda(self, expr) -> str:
        expr = str(expr)
        if "lambda" in expr:
            expr = expr.replace("lambda", "λ")
        if "Lambda" in expr:
            expr = expr.replace("Lambda", "λ")
        return expr

    def prompt_inputs(self) -> None:
        def validate(val, *args) -> bool:
            """
            Check for invalid lambda calculus expression
            """
            try:
                val = self.convert_lambda(val)
                parse_lambda_expr(val)
            except:
                return False
            return True

        expr = self.prompt_string(
            "Enter a valid lambda calculus expression (use Lambda, lambda, or "
            + "λ to represent λ) > ",
            validate,
        )
        expr = self.convert_lambda(expr)
        self.inputs["expr"] = expr


# ————————————————————————————————————————————————
# LAMBDA CALCULUS MODEL CLASS
# ————————————————————————————————————————————————


class lambda_calculus_model(solver_model):
    def solve(self) -> None:
        expr = self.inputs["expr"]
        work = parse_lambda_expr(expr)
        self.ans = str(work[-1])
        it = 1
        if len(work) == 1:
            self.work = (
                "lambda calculus expression already in weak head normal form"
            )
        else:
            self.work = (
                "Steps to reduce:\n" + "{:d}. ".format(it) + expr + "\n"
            )
            for ex in work:
                it += 1
                self.work += "{:d}. ".format(it) + str(ex) + "\n"


# Copyright 2018 Paul Crowley

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This code reused from the reduce test case in the original pylambdac project


def parse_lambda_expr(expr):
    new = []
    state = parse.parse_expr(expr)
    while state is not None:
        new.append(str(state))
        state = state.reduce_once({})
    return new
