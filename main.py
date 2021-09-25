from questionary import Separator, prompt, print
from pprint import pprint
import os
from euclidsolverfc import *

#————————————————————————————————————————————————
#GLOBAL VARIABLES
#————————————————————————————————————————————————

solver_options = ['Euclid', 'Roman', 'Exit']






#————————————————————————————————————————————————
#VISUAL HELPER FUNCTIONS
#————————————————————————————————————————————————

def clear() -> 'Clears terminal based on user OS':
    os.system('cls' if os.name == 'nt' else 'clear')

def logo() -> 'Provides the focs calc logo in the top left corner':
    print('''    __________  ___________ _________    __    ______║
   / ____/ __ \/ ____/ ___// ____/   |  / /   / ____/║
  / /_  / / / / /    \__ \/ /   / /| | / /   / /     ║
 / __/ / /_/ / /___ ___/ / /___/ ___ |/ /___/ /___   ║
/_/    \____/\____//____/\____/_/  |_/_____/\____/   ║
═════════════════════════════════════════════════════╝''', style="bold italic fg:yellow")

#————————————————————————————————————————————————
#MAINFILE QUESTION DEFINITIONS
#————————————————————————————————————————————————


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

#————————————————————————————————————————————————
#MAINFILE LOGIC
#————————————————————————————————————————————————

def menu():
    clear()
    logo()
    solver_pick = pick_solver_question()['solver_choice']
    if solver_pick == 'Exit':
        print('FOCSCalc exitting...', style="bold italic fg:yellow")
        exit()
    eval(solver_pick.lower()+'solver()')
    return menu()

menu()
