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

def prompt_input_num_candidates(**kwargs):
    questions = [
        {
            "qmark": "VOTING",
            "type": "text",
            "name": "num_candidates",
            "message": "Please enter the number of candidates (1-100) > ",
            "validate": lambda val: val.isdigit() and int(val) >= 1 and int(val) <= 100,
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


def prompt_input_num_votes(**kwargs):
    questions = [
        {
            "qmark": "VOTING",
            "type": "text",
            "name": "num_votes",
            "message": "Please enter the number of votes > (1-1000)",
            "validate": lambda val: val.isdigit() and int(val) >= 1 and int(val) <= 1000,
        },
    ]
    return prompt(questions)


def prompt_input_votes(num_votes, num_candidates, candidate_options, **kwargs):
    questions = [
        {
            "qmark": "VOTING",
            "type": "select",
            "name": "vote" + str(num_votes) + "-" + str(num_candidates),
            "message": "Vote #" + str(num_votes + 1) + ": Rank the candidates from best to worst > ",
            "choices": candidate_options
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
    
    def ans(self):
        return "Borda: " + str(self.borda()) + "\nPlurality: " + str(self.plurality())
    
    def work(self):
        pass
            
    def plurality(self):
        count = self.count.copy()
        for v in self.votes:
            count[v[0]] += 1
        return count

    def borda(self):
        count = self.count.copy()
        n = len(self.candidates)-1
        for v in self.votes: 
            for i in range(n):
                count[v[i]] += n-i
        return count


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
    num_votes = int(prompt_input_num_votes()['num_votes'])
    votes = []
    for i in range(num_votes):
        _candidates = candidates.copy()
        vote = []
        for j in range(len(candidates)):
            choice = str(prompt_input_votes(i, j, _candidates)
                         ['vote' + str(i) + "-" + str(j)])
            _candidates.remove(choice)
            vote.append(str(choice))
        votes.append(vote)
    
    solution = votingsolvermodule(candidates, votes)
    print('\nYour answer: {}'.format(solution.ans), style="bold italic fg:yellow")
    # print('Work:\n{}'.format(solution.work), style="bold italic fg:yellow")
    input('\nPlease hit enter when you are finished.')
