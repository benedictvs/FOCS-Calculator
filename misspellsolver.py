from questionary import Separator, prompt, print
from pprint import pprint
import math as m
import os

# ————————————————————————————————————————————————
# MODULE PROMPTS
#solves problems to find the number of distinct permutations of a string

# ————————————————————————————————————————————————

MAX_CHAR = 26
#Maximum word length

def prompt_word(**kwargs):
    questions = [
        {
            "qmark": "MISSPELL",
            "type": "text",
            "name": "n_input",
            "message": "How many ways can you misspell the word: (Enter word)",
            "validate": lambda val: val.isalpha(),
        },
    ]
    return prompt(questions)

def prompt_choice(**kwargs):
    questions = [
        {
            "qmark": "MISSPELL",
            "type": "text",
            "name": "k_input",
            "message": "Length of the word you want to misspell: ",
            "validate": lambda val: val.isnumeric() and int(val) > 0,
        },
    ]
    return prompt(questions)

# ————————————————————————————————————————————————
# SOLVER FUNCTIONS
# ————————————————————————————————————————————————

# Utility function to find factorial of n.
def factorial(j: int) :
     
    fact = 1;
    for i in range(2, j + 1) :
        fact = fact * i;
    return fact

def misspell(n: str, k: int) -> 'Integer':
    length = len(n)
    freq = [0] * MAX_CHAR
     
    # finding frequency of all the lower
    # case alphabet and storing them in
    # array of integer
    for i in range(0, length) :
        if (n[i] >= 'a') :
            freq[(ord)(n[i]) - 97] = freq[(ord)(n[i]) - 97] + 1;
   
    # finding factorial of number of
    # appearances and multiplying them
    # since they are repeating alphabets
    fact = 1
    for i in range(0, MAX_CHAR) :
        fact = fact * factorial(freq[i])
   
    # finding factorial of size of string
    # and dividing it by factorial found
    # after multiplying
    return factorial(length) / fact
    


def misspellwork(n: str, k: int) -> 'String':
    steps = 'Recall the Permutations equation:\n'
    steps += 'n! / (n-k)!\n'
    steps += 'Plug in our value for n (length of the word):\n'
    steps += '{}! / ({}-k)!\n'.format(len(n), len(n))
    steps += 'Finally, plug in our value for k the number of letters we want to choose and compute:\n'
    steps += '{}! / (({}-{})!)\n'.format(len(n), len(n), k)
    steps += '={} \n'.format(misspell(n,k))
    return steps


# ————————————————————————————————————————————————
# OBJECT DEFINITION OF ANSWER
# ————————————————————————————————————————————————

class misspellsolvermodule:
    def __init__(self, n: str, k: int):
        self.n = n
        self.k = k
        self.ans = misspell(n, k)
        self.work = misspellwork(n, k)

# ————————————————————————————————————————————————
# MAIN FUNCTION
# ————————————————————————————————————————————————


def misspellsolver():
    # Define the first euclid argument as global so that we can compare the second input to it
    global n_arg
    global k_arg
    n_arg = prompt_word()['n_input']
    k_arg = int(prompt_choice()['k_input'])
    solution = misspellsolvermodule(n_arg, k_arg)
    print('\nYour answer: {}'.format(solution.ans),
          style="bold italic fg:yellow")
    print('Work:\n{}'.format(solution.work), style="bold italic fg:yellow")
    input('\nPlease hit enter when you are finished.')
