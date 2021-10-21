from questionary import Separator, prompt, print
from pprint import pprint
import math as m
import os

#————————————————————————————————————————————————
#MODULE PROMPTS
#————————————————————————————————————————————————

def prompt_upper_binomial(**kwargs):
    questions = [
        {
            "qmark": "BINOMIAL",
            "type": "text",
            "name": "n_input",
            "message": "Please enter the upper value (n) > ",
            "validate": lambda val: val.isnumeric() and int(val) > 0 ,
        },
    ]
    return prompt(questions)

def prompt_lower_binomial(**kwargs):
    questions = [
        {
            "qmark": "BINOMIAL",
            "type": "text",
            "name": "k_input",
            "message": "Please enter the lower value (k) > ",
            "validate": lambda val: val.isnumeric() and int(val) > 0 and int(val) < n_arg ,
        },
    ]
    return prompt(questions)

#————————————————————————————————————————————————
#SOLVER FUNCTIONS
#————————————————————————————————————————————————

def binomial(n: int, k: int) -> 'Integer':
    return m.factorial(n) / (m.factorial(k) * (m.factorial(n-k)))

def binomialwork(n: int, k: int) -> 'String':
    steps = 'Recall the binomial coefficient equation:\n'
    steps += 'n! / (k! * (n-k!))\n'
    steps += 'Plug in our value for n:\n'
    steps += '{}! / (k! * ({}-k)!)\n'.format(n,n)
    steps += 'Finally, plug in our value for k and compute:\n'
    steps += '{}! / ({}! * ({}-{})!)\n'.format(n,k,n,k)
    steps += '={}'.format(binomial(n, k))
    return steps


#————————————————————————————————————————————————
#OBJECT DEFINITION OF ANSWER
#————————————————————————————————————————————————

class binomialsolvermodule:
    def __init__(self, n: int, k: int):
        self.n = n
        self.k = k
        self.ans = binomial(n, k)
        self.work = binomialwork(n, k)

#————————————————————————————————————————————————
#MAIN FUNCTION
#————————————————————————————————————————————————

def binomialsolver():
    #Define the first euclid argument as global so that we can compare the second input to it
    global n_arg
    n_arg = int(prompt_upper_binomial()['n_input'])
    k_arg = int(prompt_lower_binomial()['k_input'])
    solution = binomialsolvermodule(n_arg, k_arg)
    print('\nYour answer: {}'.format(solution.ans), style="bold italic fg:yellow")
    print('Work:\n{}'.format(solution.work), style="bold italic fg:yellow")
    input('\nPlease hit enter when you are finished.')
