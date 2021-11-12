import os
import sys

from questionary import prompt, print
from abstractclasses import solver

from modules.testinterfacesolver import test_solver, test_solver_model

# ————————————————————————————————————————————————
# MAIN CLASS
# ————————————————————————————————————————————————


class main:
    def __init__(self, *solvers: object) -> None:
        self.solvers = solvers
        self.solver_options = []
        for solver in solvers:
            self.solver_options.append(str(solver))
        self.solver_options.append('Exit')

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
        solver_pick = self.pick_solver_question()['solver_choice']
        if solver_pick == 'Exit':
            print('FOCSCalc exitting...', style="bold italic fg:yellow")
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
        os.system('cls' if os.name == 'nt' else 'clear')

    def logo(self) -> None:
        """
        Provides the focs calc logo in the top left corner
        """
        print('''    __________  ___________ _________    __    ______║
   / ____/ __ \/ ____/ ___// ____/   |  / /   / ____/║
  / /_  / / / / /    \__ \/ /   / /| | / /   / /     ║
 / __/ / /_/ / /___ ___/ / /___/ ___ |/ /___/ /___   ║
/_/    \____/\____//____/\____/_/  |_/_____/\____/   ║
═════════════════════════════════════════════════════╝''', style="bold italic fg:yellow")

# ————————————————————————————————————————————————
# MAINFILE QUESTION DEFINITIONS
# ————————————————————————————————————————————————

    def pick_solver_question(self):
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
In order to run the progarm, initialize your models with the module name and model class.
Then pass all your model objects into the main class initialization. Finally, Main()
runs the program. 
"""

TS = test_solver(name="Something_Else_Entirely", model=test_solver_model)

Main = main(TS)
Main()
print(str(TS))
