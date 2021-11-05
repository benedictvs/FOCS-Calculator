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
        # ————————————————————————————————————————————————
        # VETO
        # ————————————————————————————————————————————————
        count_veto, winners_veto, work_veto = self.veto()
        ret += "\nVeto: \n"
        ret += self.str_ans(count_veto, winners_veto)
        work += work_veto
        # ————————————————————————————————————————————————
        # PLURALITY WITH RUNOFF
        # ————————————————————————————————————————————————
        count_plurality_runoff, winners_plurality_runoff, work_plurality_runoff = self.veto()
        ret += "\Plurality with Runoff: \n"
        ret += self.str_ans(count_plurality_runoff, winners_plurality_runoff)
        work += work_plurality_runoff
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
                    " + (" + str(n) + " - " + str(i) +  ") * " + \
                    str(self.votes[v]) + " = " + str(score+count[v[i]])
                count[v[i]] += score

        work += "\n"
        for c in self.candidates:
            work += "\n" + str(c) + " = " + str(count[c])

        max_val = max(count.values())
        winners = [key for key, val in count.items() if val == max_val]
        return count, winners, work

    def veto(self):
        work = "\n\nVeto Voting: All candidates, save for the lowest ranking candidate," + \
            "get 1 point. The lowest ranking candidate is vetoed in each vote."
        count = self.count.copy()

        work += "\nP = "
        votes_keys = [*self.votes.keys()]
        work += str(self.votes[votes_keys[0]]) + \
            "@[" + " > ".join(votes_keys[0]) + "]"
        for i in range(1, len(votes_keys)):
            work += " + " + \
                str(self.votes[votes_keys[i]]) + \
                "@[" + " > ".join(votes_keys[i]) + "]"


        for v in self.votes:
            work += "\n\n" + str(self.votes[v]) + "@[" + " > ".join(v) + "]"
            for i in range(len(self.candidates)):
                work += "\n" + str(v[i]) + " = "
                if i != len(self.candidates)-1:
                    work += str(count[v[i]]) + " + 1 * " + str(self.votes[v]) + " = "
                    count[v[i]] += self.votes[v]
                else:
                    work += str(count[v[i]]) + " + 0 * " + str(self.votes[v]) + " = "
                work += str(count[v[i]])

        work += "\n"
        for c in self.candidates:
            work += "\n" + str(c) + " = " + str(count[c])

        max_val = max(count.values())
        winners = [key for key, val in count.items() if val == max_val]

        return count, winners, work

    def plurality_with_runoff(self):
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


def votingsolver():
    candidates = []
    num_candidates = int(prompt_input_num_candidates()['num_candidates'])
    for i in range(num_candidates):
        candidate = str(prompt_input_candidates(
            i, candidates)['candidate' + str(i)])
        candidates.append(candidate)

    vote_permutations = list(permutations(candidates))
    str_vote_permutations = vote_permutations.copy()
    for i in range(len(str_vote_permutations)):
        str_vote_permutations[i] = " > ".join(str_vote_permutations[i])

    str_vote_permutations.insert(0, "Done")
    permutation_index = str_vote_permutations.index(
        prompt_input_permutation(str_vote_permutations)['permutation'])

    votes = dict()
    while permutation_index != 0:
        num_votes = int(prompt_input_num_votes(permutation_index)[
                        "num_votes" + str(permutation_index)])

        votes[vote_permutations[permutation_index-1]] = num_votes
        str_vote_permutations.pop(permutation_index)
        vote_permutations.pop(permutation_index-1)

        permutation_index = str_vote_permutations.index(
            prompt_input_permutation(str_vote_permutations)['permutation'])

    solution = votingsolvermodule(candidates, votes)
    print('\nYour answers:\n{}'.format(solution.ans),
          style="bold italic fg:yellow")
    print('Work:\n{}'.format(solution.work), style="bold italic fg:yellow")
    input('\nPlease hit enter when you are finished.')
