from questionary import Separator, prompt, print
from pprint import pprint
from itertools import permutations
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

def prompt_input_num_candidates(**kwargs):
    questions = [
        {
            "qmark": "VOTING",
            "type": "text",
            "name": "num_candidates",
            "message": "Please enter the number of candidates (1-10) > ",
            "validate": lambda val: val.isdigit() and int(val) >= 1 and int(val) <= 10,
        },
    ]
    return prompt(questions)


def prompt_input_candidates(num_candidates, candidates, **kwargs):
    questions = [
        {
            "qmark": "VOTING",
            "type": "text",
            "name": "candidate" + str(num_candidates),
            "message": "Please enter candidate #" + str(num_candidates + 1) + " > ",
            "validate": lambda val: not (val in candidates)
        },
    ]
    return prompt(questions)


def prompt_input_permutation(vote_permutations, **kwargs):
    questions = [
        {
            "qmark": "VOTING",
            "type": "select",
            "name": "permutation",
            "message": "Which permutations have votes >",
            "choices": vote_permutations,
        },
    ]
    return prompt(questions)

def prompt_input_num_votes(num_permutation, **kwargs):
    questions = [
        {
            "qmark": "VOTING",
            "type": "text",
            "name": "num_votes" + str(num_permutation),
            "message": "Please enter the number of votes for this permutation > ",
            "validate": lambda val: val.isdigit() and int(val) >= 0,
        },
    ]
    return prompt(questions)


# ————————————————————————————————————————————————
# SOLVER FUNCTIONS
# ————————————————————————————————————————————————

class voting:
    def __init__(self, candidates: list, votes: list):
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
        # ————————————————————————————————————————————————
        # PLURALITY
        # ————————————————————————————————————————————————
        count_plurality, winners_plurality = self.plurality()
        ret += "Plurality: \n"
        ret += self.str_ans(count_plurality, winners_plurality)
        # ————————————————————————————————————————————————
        # BORDA
        # ————————————————————————————————————————————————
        count_borda, winners_borda = self.borda()
        ret += "\nBorda: \n"
        ret += self.str_ans(count_borda, winners_borda)
        return ret

    def work(self):
        pass
            
    def plurality(self):
        count = self.count.copy()
        for v in self.votes:
            count[v[0]] += 1
        max_val =  max(count.values())
        winners = [key for key, val in count.items() if val == max_val]
        return count, winners

    def borda(self):
        count = self.count.copy()
        n = len(self.candidates)-1
        for v in self.votes: 
            for i in range(n):
                count[v[i]] += n-i
        max_val =  max(count.values())
        winners = [key for key, val in count.items() if val == max_val]
        return count, winners


# ————————————————————————————————————————————————
# OBJECT DEFINITION OF ANSWER
# ————————————————————————————————————————————————

class votingsolvermodule:
    def __init__(self, candidates: list, votes: list):
        self.candidates = candidates
        self.votes = votes
        voting_model = voting(candidates, votes)
        self.ans = voting_model.ans()
        self.work = voting_model.work()

# ————————————————————————————————————————————————
# MAIN FUNCTION
# ————————————————————————————————————————————————


def votingsolver():
    candidates = []
    num_candidates = int(prompt_input_num_candidates()['num_candidates'])
    for i in range(num_candidates):
        candidate = str(prompt_input_candidates(i, candidates)['candidate' + str(i)])
        candidates.append(candidate)

    vote_permutations = list(permutations(candidates))
    str_vote_permutations = vote_permutations.copy()
    for i in range(len(str_vote_permutations)):
        str_vote_permutations[i] = " > ".join(str_vote_permutations[i])

    str_vote_permutations.insert(0, "Done")

    permutation_index = str_vote_permutations.index(prompt_input_permutation(str_vote_permutations)['permutation'])
    print(str(permutation_index))

    votes = []
    while permutation_index != 0:
        num_votes = int(prompt_input_num_votes(permutation_index)["num_votes" + str(permutation_index)])
        for _ in range(num_votes):
            votes.append(vote_permutations[permutation_index-1])
        str_vote_permutations.pop(permutation_index)
        vote_permutations.pop(permutation_index-1)
        permutation_index = str_vote_permutations.index(prompt_input_permutation(str_vote_permutations)['permutation'])
        print(str(permutation_index))
    
    solution = votingsolvermodule(candidates, votes)
    print('\nYour answers:\n{}'.format(solution.ans), style="bold italic fg:yellow")
    # print('Work:\n{}'.format(solution.work), style="bold italic fg:yellow")
    input('\nPlease hit enter when you are finished.')
