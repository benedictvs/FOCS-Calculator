import math as m
import numpy as np

from questionary import prompt, print

from abstractclasses import solver, solver_model

'''
Matrix multiplcation solves for the distance between two points in 2 or 3
dimensional space. 
'''

# ————————————————————————————————————————————————
# MATRIX MULTIPLICATION SOLVER CLASS
# ————————————————————————————————————————————————


class matrix_multiplication_solver(solver):
    def prompt_inputs(self) -> None:
        sx0_arg = self.prompt_float(
            "Please enter the width of the first matrix. (This will also be the height of the second matrix.) > ")
        sy0_arg = self.prompt_float(
            "Please enter the height of the first matrix. > ")
        sx1_arg = self.prompt_float(
            "Please enter the width of the second matrix. > ")
        sy1_arg = sx0_arg

        mat0 = [[0]*sx0_arg]*sy0_arg
        mat1 = [[0]*sx1_arg]*sy1_arg

        for x in range sx0_arg:
            for y in range sy0_arg:
                mat0[y][x] = self.prompt_float('Enter the value at {}'.format(x) + ', {}'.format(y) + ' of the first matrix.\n')

        for x in range sx1_arg:
            for y in range sy1_arg:
                mat0[y][x] = self.prompt_float('Enter the value at {}'.format(x) + ', {}'.format(y) + ' of the second matrix.\n')


        # Set inputs
        self.inputs['sx0_arg'] = sx0_arg
        self.inputs['sy0_arg'] = sy0_arg
        self.inputs['sx1_arg'] = sx1_arg
        self.inputs['sy1_arg'] = sy1_arg
        self.inputs['mat0'] = mat0
        self.inputs['mat1'] = mat1


# ————————————————————————————————————————————————
# MATRIX MULTIPLICATION MODEL CLASS
# ————————————————————————————————————————————————

class matrix_multiplication_model(solver_model):
    def solve(self) -> None:
        sx0 = self.inputs['sx0_arg']
        sy0 = self.inputs['sy0_arg']
        sx1 = self.inputs['sx1_arg']
        sy1 = self.inputs['sy1_arg']
        mat0 = self.inputs['mat0']
        mat1 = self.inputs['mat1']
        self.ans = np.matmul(mat0, mat1)
        self.work = self.matrix_multiplicationwork(sx0, sy0, sx1, sy1, mat0, mat1, '')


    def matrix_multiplicationwork(self, sx0: int, sy0: int, sx1: int, sy1: int, mat0 = [], mat1 = [], v: str) -> str:
        v += 'multiplying {}.'.format(mat0) + '\n'
        v += 'with {}.'.format(mat1) + '\n'
        v += 'We get the '\
            + 'answer: {}'.format(
                np.matmul(mat0, mat1)) + '\n'
        return v