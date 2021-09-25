from questionary import Separator, prompt, print
from pprint import pprint
import os

'''
Here is a good example of how simple it can be to add modules. This is all
based off of the Euclid solver code. This contains every single line of code
that pertains to the Roman numeral solver. The only line I had to add to the
main file, was "from romansolverfc import *". Unfortunately, the solving
functions are a little sloppy, and could use some further revision.
'''

#————————————————————————————————————————————————
#HELPER FUNCTIONS
#————————————————————————————————————————————————

def all_chars_in_set(mystr: str, myset: set) -> 'True or False':
    for i in range(0, len(mystr)):
        if not mystr[i] in myset:
            return False
    return True


#————————————————————————————————————————————————
#GLOBAL VARIABLES
#————————————————————————————————————————————————


global nums
nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}


#————————————————————————————————————————————————
#MODULE PROMPTS
#————————————————————————————————————————————————

def prompt_roman_to_dec(**kwargs):
    questions = [
        {
            "qmark": "ROMAN",
            "type": "text",
            "name": "user_input",
            "message": "Please enter the Roman numeral expression > ",
            "validate": lambda val: val.isalpha() and all_chars_in_set(val, nums) ,
        },
    ]
    return prompt(questions)


#————————————————————————————————————————————————
#SOLVER FUNCTIONS
#————————————————————————————————————————————————

def roman(expression: str) -> 'Returns integer':
    romalist = list(expression)
    if len(romalist) == 1:
        return nums[expression]
    sums = []
    for i in range(0, len(romalist)-1):
        if nums[romalist[i]] < nums[romalist[i+1]]:
            sums.append(nums[romalist[i]]*-1)
        else:
            sums.append(nums[romalist[i]])
    sums.append(nums[romalist[-1]])
    return sum(sums)

def romanwork(expression: str) -> 'Returns string containing work':
    romalist = list(expression)
    unique_romalist = set(romalist)
    unique_romalist = list(unique_romalist)
    recallstr = 'Recall that: '
    for i in range(0,len(unique_romalist)-1):
        recallstr += unique_romalist[i] + ' = ' + str(nums[unique_romalist[i]]) + ', '
    recallstr += 'and ' + unique_romalist[-1] + ' = ' + str(nums[unique_romalist[-1]])
    if len(romalist) == 1:
        return nums[expression]
    sums = []
    formula = ''
    simpleformula = ''
    for i in range(0, len(romalist)-1):
        if nums[romalist[i]] < nums[romalist[i+1]]:
            sums.append(nums[romalist[i]]*-1)
            formula += ' ' + romalist[i] + '(' + str(nums[romalist[i]]*-1) + ') +'
            simpleformula += ' ' + str(nums[romalist[i]]*-1) + ' +'
        else:
            sums.append(nums[romalist[i]])
            formula += ' ' + romalist[i] + '(' + str(nums[romalist[i]]) + ') +'
            simpleformula += ' ' + str(nums[romalist[i]]) + ' +'
    formula += ' ' + romalist[-1] + '(' + str(nums[romalist[-1]]) + ')'
    simpleformula += ' ' + str(nums[romalist[-1]])
    sums.append(nums[romalist[-1]])
    val = sum(sums)
    return recallstr + '\n' + formula + '\n' + simpleformula + '\n' + '= {}'.format(val)


#————————————————————————————————————————————————
#OBJECT DEFINITION OF ANSWER
#————————————————————————————————————————————————

class romansolvermodule:
    def __init__(self, expression: str):
        self.expression = expression
        self.ans = roman(expression)
        self.work = romanwork(expression)

#————————————————————————————————————————————————
#MAIN FUNCTION
#————————————————————————————————————————————————

def romansolver():
    #Define the first euclid argument as global so that we can compare the second input to it
    global x_arg
    exp = prompt_roman_to_dec()['user_input']

    solution = romansolvermodule(exp)
    print('\nYour answer: {}'.format(solution.ans), style="bold italic fg:yellow")
    print('Work:\n{}'.format(solution.work), style="bold italic fg:yellow")
    input('\nPlease hit enter when you are finished.')
