import os
import sys
from typing import Dict

from questionary import prompt, print

from modules.matrixmult import (
    matrix_multiplication_model,
    matrix_multiplication_solver,
)
from modules.votingsystems import voting_systems_solver, voting_systems_model
from modules.binomialcoefficient import (
    binomial_coefficient_solver,
    binomial_coefficient_model,
)
from modules.euclidiandivision import (
    euclidian_division_solver,
    euclidian_division_model,
)
from modules.vectordistance import (
    vector_distance_solver,
    vector_distance_model,
)
from modules.romannumeral import roman_numeral_solver, roman_numeral_model
from modules.misspellcombinations import (
    misspell_combinations_solver,
    mispell_combinations_model,
)
from modules.nashequillibrium import (
    nash_equillibrium_solver,
    nash_equillibrium_model,
)
from modules.conditionalprobability import (
    conditional_probability_solver,
    conditional_probability_model,
)
from modules.logicgate import logic_gate_solver, logic_gate_model
from modules.modulararithmetic import (
    modular_arithmetic_solver,
    modular_arithmetic_model,
)
from modules.lambdacalculus import (
    lambda_calculus_solver,
    lambda_calculus_model,
)

# ————————————————————————————————————————————————
# MAIN CLASS
# ————————————————————————————————————————————————


class main:
    def __init__(self, *solvers: object) -> None:
        self.solvers = solvers
        self.solver_options = []
        for solver in solvers:
            self.solver_options.append(str(solver))
        self.solver_options.append("Exit")

    def __call__(self) -> None:
        self.menu()

    # ————————————————————————————————————————————————
    # MENU LOGIC
    # ————————————————————————————————————————————————

    def menu(self) -> None:
        """
        Recursive Main Menu Function calls other helper functions
        """
        self.clear()
        self.logo()
        solver_pick = self.pick_solver_question()["solver_choice"]
        if solver_pick == "Exit":
            print("FOCSCalc exitting...", style="bold italic fg:yellow")
            sys.exit(0)
        self.solvers[self.solver_options.index(solver_pick)]()
        return self.menu()

    # ————————————————————————————————————————————————
    # VISUAL HELPER FUNCTIONS
    # ————————————————————————————————————————————————

    def clear(self) -> None:
        """
        Clears terminal based on user OS'
        """
        os.system("cls" if os.name == "nt" else "clear")

    def logo(self) -> None:
        """
        Provides the focs calc logo in the top left corner
        """
        print(
            """    __________  ___________ _________    __    ______║
   / ____/ __ \\/ ____/ ___// ____/   |  / /   / ____/║
  / /_  / / / / /    \\__ \\/ /   / /| | / /   / /     ║
 / __/ / /_/ / /___ ___/ / /___/ ___ |/ /___/ /___   ║
/_/    \\____/\\____//____/\\____/_/  |_/_____/\\____/   ║
═════════════════════════════════════════════════════╝""",
            style="bold italic fg:yellow",
        )

    # ————————————————————————————————————————————————
    # MAINFILE QUESTION DEFINITIONS
    # ————————————————————————————————————————————————

    def pick_solver_question(self) -> Dict:
        questions = [
            {
                "qmark": "FC",
                "type": "select",
                "name": "solver_choice",
                "message": "Which type of question would you like to solve?",
                "choices": self.solver_options,
            },
        ]
        return prompt(questions)


# ————————————————————————————————————————————————
# MAIN CLASS AND MODULE INITIALIZATION
# ————————————————————————————————————————————————
"""
In order to run the progarm, initialize your models with the module name
and model class. Then pass all your model objects into the main class
initialization. Finally, Main() runs the program.
"""

voting = voting_systems_solver(
    name="Voting Systems", model=voting_systems_model
)
binomial_coefficient = binomial_coefficient_solver(
    name="Binomial Coefficient", model=binomial_coefficient_model
)
euclidian_division = euclidian_division_solver(
    name="Euclidian Division", model=euclidian_division_model
)
vector_distance = vector_distance_solver(
    name="Vector Distance", model=vector_distance_model
)
roman_numeral = roman_numeral_solver(
    name="Roman Numeral", model=roman_numeral_model
)
matrix_multiplication = matrix_multiplication_solver(
    name="Matrix Multiplication", model=matrix_multiplication_model
)
misspell_combinations = misspell_combinations_solver(
    name="Misspell Combinations", model=mispell_combinations_model
)
nash_equillibrium = nash_equillibrium_solver(
    name="Nash Equillibrium", model=nash_equillibrium_model
)
conditional_probability = conditional_probability_solver(
    name="Conditional Probability", model=conditional_probability_model
)
logic_gate = logic_gate_solver(name="Logic Gates", model=logic_gate_model)
lambda_calculus = lambda_calculus_solver(
    name="Lambda Calculus", model=lambda_calculus_model
)
modular_arithmetic = modular_arithmetic_solver(
    name="Modular Artithmetic", model=modular_arithmetic_model
)

_main = main(
    binomial_coefficient,
    conditional_probability,
    euclidian_division,
    lambda_calculus,
    logic_gate,
    matrix_multiplication,
    misspell_combinations,
    modular_arithmetic,
    nash_equillibrium,
    roman_numeral,
    vector_distance,
    voting,
)
_main()
