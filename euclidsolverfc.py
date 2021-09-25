from questionary import Separator, prompt, print
from pprint import pprint
import os

'''
This is the entirety of the Euclid solver. We have two different questionary prompts
defined, so that we can compare them to eachother. If the prompts were combined into
one, I could not validate that the second input was greater than the first, because
questionary does not make the answer variables readable until after the prompt is
finished. We also make sure to display all output text within our main function, so
we don't clutter out main FOCSCalc file.
'''



#————————————————————————————————————————————————
#MODULE PROMPTS
#————————————————————————————————————————————————

def prompt_input_x(**kwargs):
    questions = [
        {
            "qmark": "EUCLID",
            "type": "text",
            "name": "x_input",
            "message": "Please enter the first value > ",
            "validate": lambda val: val.isnumeric() ,
        },
    ]
    return prompt(questions)

def prompt_input_y(**kwargs):
    questions = [
        {
            "qmark": "EUCLID",
            "type": "text",
            "name": "y_input",
            "message": "Please enter the second value > ",
            #In Euclid's algorithm, the second value must always be greater
            #This double lambda statement assures that it is numeric and greater
            "validate": lambda val: val.isnumeric() and int(val) > x_arg ,
        },
    ]
    return prompt(questions)

#————————————————————————————————————————————————
#SOLVER FUNCTIONS
#————————————————————————————————————————————————

def euclid(x: int, y: int) -> 'Recursive function, returns integer answer when done':
    if y == 0:
        return x
    else:
        return euclid(y, x%y)

def euclidwork(x: int, y: int, v: str) -> 'Recursive function, returns string of work when done':
    if y == 0:
        v += 'Final GCD is {}'.format(x)
        return v
    else:
        if x > y and x%y != 0:
            v += '{} goes into {} {} times, with a remainder of {}. Now perform gcd({}, {})'.format(y, x, x//y, x%y, x%y, y) + '\n'
        elif x > y and x%y == 0:
            v += '{} goes into {} {} times, with a remainder of {}. We have arrived at our GCD.'.format(y, x, x//y, x%y) + '\n'
        return euclidwork(y, x%y, v)


#————————————————————————————————————————————————
#OBJECT DEFINITION OF ANSWER
#————————————————————————————————————————————————

class euclidsolvermodule:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.ans = euclid(x, y)
        self.work = euclidwork(x, y, '')

#————————————————————————————————————————————————
#MAIN FUNCTION
#————————————————————————————————————————————————

def euclidsolver():
    #Define the first euclid argument as global so that we can compare the second input to it
    global x_arg
    x_arg = int(prompt_input_x()['x_input'])
    y_arg = int(prompt_input_y()['y_input'])

    solution = euclidsolvermodule(x_arg, y_arg)
    print('\nYour answer: {}'.format(solution.ans), style="bold italic fg:yellow")
    print('Work:\n{}'.format(solution.work), style="bold italic fg:yellow")
    input('\nPlease hit enter when you are finished.')
