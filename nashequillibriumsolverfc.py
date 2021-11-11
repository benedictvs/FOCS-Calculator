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

class voting:
    def __init__(self, candidates: list, votes: dict):
        self.candidates = candidates
        self.votes = votes
        self.count = dict()
        for c in self.candidates:
            self.count[c] = 0

    def str_ans(self, count, winners):
        ret = ""
        for c in self.candidates:
            ret += "\t" + str(c) + ": " + str(count[c]) + "\n"
        if len(winners) == 1:
            ret += "\tWinner: " + winners[0]
        else:
            ret += "\tWinners: " + ", ".join(winners)
        return ret

    def ans(self):
        ret = ""
        work = ""
        # ————————————————————————————————————————————————
        # PLURALITY
        # ————————————————————————————————————————————————
        count_plurality, winners_plurality, work_plurality = self.plurality()
        ret += "Plurality: \n"
        ret += self.str_ans(count_plurality, winners_plurality)
        work += work_plurality
        # ————————————————————————————————————————————————
        # BORDA
        # ————————————————————————————————————————————————
        count_borda, winners_borda, work_borda = self.borda()
        ret += "\nBorda: \n"
        ret += self.str_ans(count_borda, winners_borda)
        work += work_borda
        return ret, work

    def plurality(self):
        work = "Plurality Voting: The highest ranked candidate gets 1 point; " + \
            "all other candidates get 0 points."
        work += "\nP = "
        count = self.count.copy()

        votes_keys = [*self.votes.keys()]
        work += str(self.votes[votes_keys[0]]) + \
            "@[" + " > ".join(votes_keys[0]) + "]"
        for i in range(1, len(votes_keys)):
            work += " + " + \
                str(self.votes[votes_keys[i]]) + \
                "@[" + " > ".join(votes_keys[i]) + "]"

        for v in self.votes:
            work += "\n\n" + str(self.votes[v]) + "@[" + " > ".join(v) + "]"
            work += "\n" + str(v[0]) + " = " + \
                str(count[v[0]]) + " + " + str(self.votes[v])
            count[v[0]] += self.votes[v]
            work += " = " + str(count[v[0]])

        work += "\n"
        for c in self.candidates:
            work += "\n" + str(c) + " = " + str(count[c])

        max_val = max(count.values())
        winners = [key for key, val in count.items() if val == max_val]
        return count, winners, work

    def borda(self):
        work = "\n\nBorda Voting: The lowest ranked candidate gets 0 points, " + \
            "the next lowest gets 1, up to the highest candidate who gets n-1 " + \
            "votes, where n is the number of candidates."
        work += "\nP = "
        count = self.count.copy()

        n = len(self.candidates)-1

        votes_keys = [*self.votes.keys()]
        work += str(self.votes[votes_keys[0]]) + \
            "@[" + " > ".join(votes_keys[0]) + "]"
        for i in range(1, len(votes_keys)):
            work += " + " + \
                str(self.votes[votes_keys[i]]) + \
                "@[" + " > ".join(votes_keys[i]) + "]"

        for v in self.votes:
            work += "\n\n" + str(self.votes[v]) + "@[" + " > ".join(v) + "]"
            for i in range(n+1):
                score = (n-i) * self.votes[v]
                work += "\n" + str(v[i]) + " = "
                work += str(count[v[i]]) + \
                    " + " + str(n-i) + " * " + \
                    str(self.votes[v]) + " = " + str(score+count[v[i]])
                count[v[i]] += score

        work += "\n"
        for c in self.candidates:
            work += "\n" + str(c) + " = " + str(count[c])

        max_val = max(count.values())
        winners = [key for key, val in count.items() if val == max_val]
        print(work)
        return count, winners, work

    def veto(self):
        pass

# ————————————————————————————————————————————————
# OBJECT DEFINITION OF ANSWER
# ————————————————————————————————————————————————


class votingsolvermodule:
    def __init__(self, candidates: list, votes: dict):
        self.candidates = candidates
        self.votes = votes
        voting_model = voting(candidates, votes)
        ans, work = voting_model.ans()
        self.ans = ans
        self.work = work

# ————————————————————————————————————————————————
# MAIN FUNCTION
# ————————————————————————————————————————————————


def print_payoff_matrix(payoff_matrix):
    player_1_strategies = ["A", "B", "C", "D", "E",
                           "F", "G", "H", "I", "J", "K", "L", "M"]
    player_2_strategies = ["N", "O", "P", "Q", "R",
                           "S", "T", "U", "V", "W", "X", "Y", "Z"]
    print("\t    Player 1")
    print("\t          " + player_1_strategies[0] + "            ", end="")
    for j in range(1, len(payoff_matrix[0])):
        print(player_1_strategies[j] + "            ", end="")
    print("")
    print("\t    +------------+", end="")
    for j in range(1, len(payoff_matrix[0])):
        print("------------+", end="")
    print("")
    print("Player 2  " + str(player_2_strategies[0]) + " |", end="")
    for j in range(len(payoff_matrix[0])):
        print("{:>5g}, {:<5g}".format(
            payoff_matrix[0][j][0], payoff_matrix[0][j][1]), end="|")
    print("")
    for i in range(1, len(payoff_matrix)):
        print("\t    +------------+", end="")
        for j in range(1, len(payoff_matrix[0])):
            print("------------+", end="")
        print("")
        print("\t  " + player_2_strategies[i] + " |" + "{:>5g}, {:<5g}".format(
            payoff_matrix[i][0][0], payoff_matrix[i][0][1]), end="|")
        for j in range(1, len(payoff_matrix[i])):
            print("{:>5g}, {:<5g}".format(
                payoff_matrix[i][j][0], payoff_matrix[i][j][1]), end="|")
        print("")
    print("\t    +------------+", end="")
    for j in range(1, len(payoff_matrix[0])):
        print("------------+", end="")
    print("")


def nashsolver():
    player_1_strategies = ["A", "B", "C", "D", "E",
                           "F", "G", "H", "I", "J", "K", "L", "M"]
    player_2_strategies = ["N", "O", "P", "Q", "R",
                           "S", "T", "U", "V", "W", "X", "Y", "Z"]
    num_strategies_1 = int(prompt_input_num_strategies_1()['num_strategies_1'])
    num_strategies_2 = int(prompt_input_num_strategies_2()['num_strategies_2'])
    payoff_matrix = [[(0, 0) for i in range(num_strategies_1)]
                     for j in range(num_strategies_2)]
    print(str(payoff_matrix))
    print_payoff_matrix(payoff_matrix)
    for i in range(num_strategies_2):
        for j in range(num_strategies_1):
            player_1_payoff = float(prompt_input_payoff(1, player_1_strategies[j], player_2_strategies[i])[
                                    'payoff1' + str(player_1_strategies[j]) + str(player_2_strategies[i])])
            player_2_payoff = float(prompt_input_payoff(2, player_1_strategies[j], player_2_strategies[i])[
                                    'payoff2' + str(player_1_strategies[j]) + str(player_2_strategies[i])])
            payoff_matrix[i][j] = (player_1_payoff, player_2_payoff)
            print_payoff_matrix(payoff_matrix)

    # vote_permutations = list(permutations(candidates))
    # str_vote_permutations = vote_permutations.copy()
    # for i in range(len(str_vote_permutations)):
    #     str_vote_permutations[i] = " > ".join(str_vote_permutations[i])

    # str_vote_permutations.insert(0, "Done")
    # permutation_index = str_vote_permutations.index(
    #     prompt_input_permutation(str_vote_permutations)['permutation'])

    # votes = dict()
    # while permutation_index != 0:
    #     num_votes = int(prompt_input_num_votes(permutation_index)[
    #                     "num_votes" + str(permutation_index)])

    #     votes[vote_permutations[permutation_index-1]] = num_votes
    #     str_vote_permutations.pop(permutation_index)
    #     vote_permutations.pop(permutation_index-1)

    #     permutation_index = str_vote_permutations.index(
    #         prompt_input_permutation(str_vote_permutations)['permutation'])

    # solution = votingsolvermodule(candidates, votes)
    # print('\nYour answers:\n{}'.format(solution.ans),
    #       style="bold italic fg:yellow")
    # print('Work:\n{}'.format(solution.work), style="bold italic fg:yellow")
    input('\nPlease hit enter when you are finished.')
