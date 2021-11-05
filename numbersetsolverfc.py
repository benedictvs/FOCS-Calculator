from questionary import Separator, prompt, print
from pprint import pprint
import math as m
import os
import sys

'''
Numberset solver is extremely complex and still unstable
'''

# ————————————————————————————————————————————————
# GLOBAL VARIABLES
# ————————————————————————————————————————————————


global operation_types
operation_types = ['Contains', 'Divisible By', 'Ends With']


# ————————————————————————————————————————————————
# MODULE PROMPTS
# ————————————————————————————————————————————————

def pick_operation(**kwargs):
    questions = [
        {
            "qmark": "NUMBERSET",
            "type": "select",
            "name": "numberset_type",
            "message": "Please choose which operation you would like to perform.",
            "choices": operation_types,
        },
    ]
    return prompt(questions)


def define_lower_bound(**kwargs):
    questions = [
        {
            "qmark": "NUMBERSET",
            "type": "text",
            "name": "lower_bound",
            "message": "Please enter the lower value in the set > ",
            "validate": lambda val: val.isnumeric(),
        },
    ]
    return prompt(questions)


def define_upper_bound(**kwargs):
    questions = [
        {
            "qmark": "NUMBERSET",
            "type": "text",
            "name": "upper_bound",
            "message": "Please enter the higher value in the set > ",
            "validate": lambda val: val.isnumeric() and val > lower_bound,
        },
    ]
    return prompt(questions)


def define_value_amt(**kwargs):
    questions = [
        {
            "qmark": "NUMBERSET",
            "type": "text",
            "name": "val_amt",
            "message": "Please enter the amount of values that we will be working with > ",
            "validate": lambda val: val.isnumeric() and val > 0,
        },
    ]
    return prompt(questions)
# ————————————————————————————————————————————————
# SOLVER FUNCTIONS
# ————————————————————————————————————————————————


'''
Currently testing this locally
'''


# ————————————————————————————————————————————————
# OBJECT DEFINITION OF ANSWER
# ————————————————————————————————————————————————

class numbersetsolvermodule:
    def __init__(self, lower: int, upper: int, val_amt: int, values: list):
        self.lower = lower
        self.upper = upper
        self.val_amt = val_amt
        self.values = values
        self.ans = numberset(lower, upper, val_amt, values)
        self.work = numbersetwork(lower, upper, val_amt, values)

# ————————————————————————————————————————————————
# MAIN FUNCTION
# ————————————————————————————————————————————————


def numbersetsolver():
    # Define the first euclid argument as global so that we can compare the second input to it
    global lower_bound
    lower_bound = int(define_lower_bound()['lower_bound'])
    global upper_bound
    upper_bound = int(define_upper_bound()['upper_bound'])
    global val_amt
    val_amt = int(define_value_amt()['val_amt'])

    solution = numbersetsolvermodule(x_arg, y_arg)
    print('\nYour answer: {}'.format(solution.ans),
          style="bold italic fg:yellow")
    print('Work:\n{}'.format(solution.work), style="bold italic fg:yellow")
    input('\nPlease hit enter when you are finished.')
