from questionary import Separator, prompt, print
import sys
import os
import math as m
from pprint import pprint
from solverfc import solver, solver_model


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


# ————————————————————————————————————————————————
# GLOBAL VARIABLES
# ————————————————————————————————————————————————

solver_options = ['Test', 'Exit']


# ————————————————————————————————————————————————
# VISUAL HELPER FUNCTIONS
# ————————————————————————————————————————————————

def clear() -> 'Clears terminal based on user OS':
    os.system('cls' if os.name == 'nt' else 'clear')


def logo() -> 'Provides the focs calc logo in the top left corner':
    print('''    __________  ___________ _________    __    ______║
   / ____/ __ \/ ____/ ___// ____/   |  / /   / ____/║
  / /_  / / / / /    \__ \/ /   / /| | / /   / /     ║
 / __/ / /_/ / /___ ___/ / /___/ ___ |/ /___/ /___   ║
/_/    \____/\____//____/\____/_/  |_/_____/\____/   ║
═════════════════════════════════════════════════════╝''', style="bold italic fg:yellow")

# ————————————————————————————————————————————————
# MAINFILE QUESTION DEFINITIONS
# ————————————————————————————————————————————————


def pick_solver_question(**kwargs):
    questions = [
        {
            "qmark": "FC",
            "type": "select",
            "name": "solver_choice",
            "message": "Which type of question would you like to solve?",
            "choices": solver_options,
        },
    ]
    return prompt(questions)

# ————————————————————————————————————————————————
# MAINFILE LOGIC
# ————————————————————————————————————————————————


def menu():
    clear()
    logo()
    solver_pick = pick_solver_question()['solver_choice']
    if solver_pick == 'Exit':
        print('FOCSCalc exitting...', style="bold italic fg:yellow")
        sys.exit(0)
    TS = test_solver("Test",test_solver_model)
    TS()
    return menu()


menu()
