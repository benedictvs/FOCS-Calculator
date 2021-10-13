from questionary import Separator, prompt, print
from pprint import pprint
import os

'''
This is the work in progress for the vector distance solver.
'''



#————————————————————————————————————————————————
#MODULE PROMPTS
#————————————————————————————————————————————————

def prompt_input_x(**kwargs):
    questions = [
        {
            "qmark": "DISTANCE",
            "type": "text",
            "name": "x0_input",
            "message": "Please enter the x value of the first point > ",
            "validate": lambda val: val.isnumeric() ,
        },
        {
            "qmark": "DISTANCE",
            "type": "text",
            "name": "y0_input",
            "message": "Please enter the y value of the first point > ",
            "validate": lambda val: val.isnumeric() ,
        },
        {
            "qmark": "DISTANCE",
            "type": "text",
            "name": "z0_input",
            "message": "Please enter the z value of the first point (enter 0 if 2D) > ",
            "validate": lambda val: val.isnumeric() ,
        },
    ]
    return prompt(questions)

def prompt_input_y(**kwargs):
    questions = [
        {
            "qmark": "VECTOR DISTANCE",
            "type": "text",
            "name": "x1_input",
            "message": "Please enter the x value of the second point > ",
            "validate": lambda val: val.isnumeric() ,
        },
        {
            "qmark": "VECTOR DISTANCE",
            "type": "text",
            "name": "y1_input",
            "message": "Please enter the y value of the second point > ",
            "validate": lambda val: val.isnumeric() ,
        },
        {
            "qmark": "VECTOR DISTANCE",
            "type": "text",
            "name": "z1_input",
            "message": "Please enter the z value of the second point (enter 0 if 2D) > ",
            "validate": lambda val: val.isnumeric() ,
        },
    ]
    return prompt(questions)

#————————————————————————————————————————————————
#SOLVER FUNCTIONS
#————————————————————————————————————————————————

def distance(x0: int, y0: int, z0: int, x1: int, y1: int, z1: int) -> 'Function will return the answer when done':
    squared = (x0 - x1)^2 + (y0 - y1)^2 + (z0 - z1)^2
    return sqrt(squared)

def distancework(x0: int, y0: int, z0: int, x1: int, y1: int, z1: int, v: str) -> 'Function will return a string showing work when done':
    v += 'x squared is {}.'.format((x1-x0)^2) + '\n'
    v += 'y squared is {}.'.format((y1-y0)^2) + '\n'
    v += 'z squared is {}.'.format((z1-z0)^2) + '\n'
    squared = (x0 - x1)^2 + (y0 - y1)^2 + (z0 - z1)^2
    v += 'add x squared, y squared, and z squared together to get the answer: {}'.format(sqrt(squared)) + '\n'
    return v

#————————————————————————————————————————————————
#OBJECT DEFINITION OF ANSWER
#————————————————————————————————————————————————

class distancesolvermodule:
    def __init__(self, x0: int, y0: int, z0: int, x1: int, y1: int, z1: int):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.ans = distance(x0, y0, z0, x1, y1, z1)
        self.work = distancework(x0, y0, z0, x1, y1, z1, '')

#————————————————————————————————————————————————
#MAIN FUNCTION
#————————————————————————————————————————————————

def distancesolver():
    x0_arg = int(prompt_input_x0()['x0_input'])
    y0_arg = int(prompt_input_y0()['y0_input'])
    z0_arg = int(prompt_input_z0()['z0_input'])
    x1_arg = int(prompt_input_x1()['x1_input'])
    y1_arg = int(prompt_input_y1()['y1_input'])
    z1_arg = int(prompt_input_z1()['z1_input'])

    solution = euclidsolvermodule(x0_arg, y0_arg, z0_arg, x1_arg, y1_arg, z1_arg)
    print('\nYour answer: {}'.format(solution.ans), style="bold italic fg:yellow")
    print('Work:\n{}'.format(solution.work), style="bold italic fg:yellow")
    input('\nPlease hit enter when you are finished.')