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


# ————————————————————————————————————————————————
# MODULE PROMPTS
# ————————————————————————————————————————————————

def prompt_input_num_strategies_1(**kwargs):
    questions = [
        {
            "qmark": "NASH",
            "type": "text",
            "name": "num_strategies_1",
            "message": "Please enter the number of strategies for player 1 (2-13) > ",
            "validate": lambda val: val.isdigit() and int(val) >= 2 and int(val) <= 13,
        },
    ]
    return prompt(questions)


def prompt_input_num_strategies_2(**kwargs):
    questions = [
        {
            "qmark": "NASH",
            "type": "text",
            "name": "num_strategies_2",
            "message": "Please enter the number of strategies for player 2 (2-13) > ",
            "validate": lambda val: val.isdigit() and int(val) >= 2 and int(val) <= 13,
        },
    ]
    return prompt(questions)


def prompt_input_payoff(player, x, y, **kwargs):
    questions = [
        {
            "qmark": "NASH",
            "type": "text",
            "name": "payoff" + str(player) + str(x) + str(y),
            "message": "Please enter the payoff value for Player " + str(player) + " in cell " + str(x) + ", " + str(y) + " of the payoff matrix > ",
            "validate": lambda val: isFloat(val),
        },
    ]
    return prompt(questions)


def isFloat(a):
    try:
        float(a)
    except:
        return False
    return True


# ————————————————————————————————————————————————
# SOLVER FUNCTIONS
# ————————————————————————————————————————————————

def nash(payoff_matrix, player_1_strategies, player_2_strategies):
    work = ""

    no_dominant_exists = False
    while not no_dominant_exists and not (len(player_1_strategies) == 1 and len(player_2_strategies) == 1):
        is_break = False
        for i in range(len(payoff_matrix)):
            for j in range(len(payoff_matrix)):
                if i != j and i < len(payoff_matrix[0]) and j < len(payoff_matrix[0]):
                    is_greater = False
                    for k in range(len(payoff_matrix[0])):
                        if float(payoff_matrix[i][k][0]) > float(payoff_matrix[j][k][0]):
                            is_greater = True
                        if is_greater:
                            break
                    if not is_greater:
                        work += "Player 2's Strategy " + str(
                            player_2_strategies[j]) + " dominates strategy " + str(player_2_strategies[i]) + '\n'
                        payoff_matrix.pop(i)
                        player_2_strategies.pop(i)
                        is_break = True
                        work += format_payoff_matrix(
                            payoff_matrix, player_1_strategies, player_2_strategies)
                        break
                if is_break:
                    break

        if is_break:
            no_dominant_exists = False

        is_break = False
        for i in range(len(payoff_matrix[0])):
            for j in range(len(payoff_matrix[0])):
                if i != j and i < len(payoff_matrix[0]) and j < len(payoff_matrix[0]):
                    is_greater = False
                    for k in range(len(payoff_matrix)):
                        if float(payoff_matrix[k][i][1]) > float(payoff_matrix[k][j][1]):
                            is_greater = True
                        if is_greater:
                            break
                    if not is_greater:
                        work += "Player 1's Strategy " + str(
                            player_1_strategies[j]) + " dominates strategy " + str(player_1_strategies[i]) + '\n'
                        for l in range(len(payoff_matrix)):
                            payoff_matrix[l].pop(i)
                        player_1_strategies.pop(i)
                        work += format_payoff_matrix(
                            payoff_matrix, player_1_strategies, player_2_strategies) 
                        is_break = True
                        break
                if is_break:
                    break

        if is_break:
            no_dominant_exists = False

    if not (len(player_1_strategies) == 1 and len(player_2_strategies) == 1):
        ans = "There is no Nash Equillibrium, since at least one player has multiple viable strategies.\n"
        work += ans
    else:
        ans = "This is the Nash Equillibrium of the entered payoff matrix, calculated by eliminating dominanted strategies.\n"
        ans += format_payoff_matrix(
            payoff_matrix, player_1_strategies, player_2_strategies)
        work += ans
    return ans, work

# ————————————————————————————————————————————————
# OBJECT DEFINITION OF ANSWER
# ————————————————————————————————————————————————


class nashsolvermodule:
    def __init__(self, payoff_matrix: list, player_1_strategies: int, player_2_strategies: int):
        self.player_1_strategies = player_1_strategies
        self.player_2_strategies = player_2_strategies
        self.ans, self.work = nash(payoff_matrix, player_1_strategies,
                        player_2_strategies)

# ————————————————————————————————————————————————
# MAIN FUNCTION
# ————————————————————————————————————————————————


def print_payoff_matrix(payoff_matrix, player_1_strategies, player_2_strategies):
    print(format_payoff_matrix(payoff_matrix,
          player_1_strategies, player_2_strategies))

def print_payoff_matrix(payoff_matrix, player_1_strategies, player_2_strategies):
    print(format_payoff_matrix(payoff_matrix, player_1_strategies, player_2_strategies))

def format_payoff_matrix(payoff_matrix, player_1_strategies, player_2_strategies):
    ret = "\t    Player 1\n"
    ret += "\t          " + player_1_strategies[0] + "            "
    for j in range(1, len(payoff_matrix[0])):
        ret += player_1_strategies[j] + "            "
    ret += '\n'
    ret += "\t    +------------+"
    for j in range(1, len(payoff_matrix[0])):
        ret += "------------+"
    ret += '\n'
    ret += "Player 2  " + str(player_2_strategies[0]) + " |"
    for j in range(len(payoff_matrix[0])):
        ret += "{:>5g}, {:<5g}".format(
            payoff_matrix[0][j][0], payoff_matrix[0][j][1]) + '|'
    ret += '\n'
    for i in range(1, len(payoff_matrix)):
        ret += "\t    +------------+"
        for j in range(1, len(payoff_matrix[0])):
            ret += "------------+"
        ret += '\n'
        ret += "\t  " + player_2_strategies[i] + " |" + "{:>5g}, {:<5g}".format(
            payoff_matrix[i][0][0], payoff_matrix[i][0][1]) + '|'
        for j in range(1, len(payoff_matrix[i])):
            ret += "{:>5g}, {:<5g}".format(
                payoff_matrix[i][j][0], payoff_matrix[i][j][1]) + '|'
        ret += '\n'
    ret += "\t    +------------+"
    for j in range(1, len(payoff_matrix[0])):
        ret += "------------+"
    ret += '\n'
    return ret


def nashsolver():
    player_1_strategies = ["A", "B", "C", "D", "E",
                           "F", "G", "H", "I", "J", "K", "L", "M"]
    player_2_strategies = ["N", "O", "P", "Q", "R",
                           "S", "T", "U", "V", "W", "X", "Y", "Z"]
    num_strategies_1 = int(prompt_input_num_strategies_1()['num_strategies_1'])
    num_strategies_2 = int(prompt_input_num_strategies_2()['num_strategies_2'])

    player_1_strategies = player_1_strategies[:num_strategies_1]
    player_2_strategies = player_2_strategies[:num_strategies_2]

    payoff_matrix = [[(0, 0) for i in range(num_strategies_1)]
                     for j in range(num_strategies_2)]
    print_payoff_matrix(payoff_matrix, player_1_strategies,
                        player_2_strategies)
    for i in range(num_strategies_2):
        for j in range(num_strategies_1):
            player_1_payoff = float(prompt_input_payoff(1, player_1_strategies[j], player_2_strategies[i])[
                                    'payoff1' + str(player_1_strategies[j]) + str(player_2_strategies[i])])
            player_2_payoff = float(prompt_input_payoff(2, player_1_strategies[j], player_2_strategies[i])[
                                    'payoff2' + str(player_1_strategies[j]) + str(player_2_strategies[i])])
            payoff_matrix[i][j] = (player_2_payoff, player_1_payoff)
            print_payoff_matrix(
                payoff_matrix, player_1_strategies, player_2_strategies)

    solution = nashsolvermodule(
        payoff_matrix, player_1_strategies, player_2_strategies)
    print('\nYour answers:\n{}'.format(solution.ans),
          style="bold italic fg:yellow")
    print('Work:\n{}'.format(solution.work), style="bold italic fg:yellow")
    input('\nPlease hit enter when you are finished.')
