from itertools import permutations

from questionary import print

from abstractclasses import solver, solver_model
'''
The Voting Systems Module takes a number of ranked votes, then it solves      
for the winner of an election, given some voting system.

For now, the system implements the following systems:

Borda - top candidate gets n-1 points, second gets n-2... to the bottom 
        candidate who gets 0
Plurality - top candidate gets 1 point; all others get 0
'''

# ————————————————————————————————————————————————
# VOTING SYSTEMS MODEL CLASS
# ————————————————————————————————————————————————


class voting_systems_solver_model(solver_model):
    def __init__(self, **inputs) -> None:
        super().__init__(**inputs)
        self.candidates = self.inputs['candidates']
        self.votes = self.inputs['votes']
        self.count = dict()
        for c in self.candidates:
            self.count[c] = 0

    def solve(self) -> None:
        """
        Calls the different helper functions to take inputs and solve
        """
        ans = ""
        work = ""
        # ————————————————————————————————————————————————
        # PLURALITY
        # ————————————————————————————————————————————————
        count_plurality, winners_plurality, work_plurality = self.plurality()
        ans += "Plurality: \n"
        ans += self.str_ans(count_plurality, winners_plurality)
        work += work_plurality
        # ————————————————————————————————————————————————
        # BORDA
        # ————————————————————————————————————————————————
        count_borda, winners_borda, work_borda = self.borda()
        ans += "\nBorda: \n"
        ans += self.str_ans(count_borda, winners_borda)
        work += work_borda

        # Setting outputs
        self.ans = ans
        self.work = work

    def str_ans(self, count: list, winners: list) -> str:
        """
        Convert the answer to string
        """
        ret = ""
        for c in self.candidates:
            ret += "\t" + str(c) + ": " + str(count[c]) + "\n"
        if len(winners) == 1:
            ret += "\tWinner: " + winners[0]
        else:
            ret += "\tWinners: " + ", ".join(winners)
        return ret

    def borda(self) -> tuple:
        """
        calculates the winners, the count of how many points candidates got,
        and the work needed to get those answers under Borda voting
        """
        work = "\n\nBorda Voting: The lowest ranked candidate gets 0 "\
            + "points, the next lowest gets 1, up to the highest  "\
            + "candidate who gets n-1 votes, where n is the number of "\
            + "candidates."
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

    def plurality(self) -> tuple:
        """
        calculates the winners, the count of how many points candidates got, 
        and the work needed to get those answers under Plurality voting
        """
        work = "Plurality Voting: The highest ranked candidate gets 1 " + \
            "point; all other candidates get 0 points."
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

# ————————————————————————————————————————————————
# VOTING SYSTEMS SOLVER CLASS
# ————————————————————————————————————————————————


class voting_systems_solver(solver):
    def prompt_inputs(self) -> None:
        candidates = []

        num_candidates = self.prompt_integer(
            "Please enter the number of candidates (1-10) > ", 1, 10)
        for i in range(num_candidates):
            message_text = "Please enter candidate #" + str(i+1)

            # Validate function for candidate prompt
            validate = lambda val, *args: not (val in args[0][0])

            candidate = str(self.prompt_string(
                message_text, validate, candidates))
            candidates.append(candidate)

        vote_permutations = list(permutations(candidates))
        str_vote_permutations = vote_permutations.copy()
        for i in range(len(str_vote_permutations)):
            str_vote_permutations[i] = " > ".join(str_vote_permutations[i])

        str_vote_permutations.insert(0, "Done")
        permutation_index = str_vote_permutations.index(
            self.prompt_choices("Which permutations have votes >",
                                str_vote_permutations))

        votes = dict()
        while permutation_index != 0:
            num_votes = int(self.prompt_integer(
                "Please enter the number of votes for this permutation > ",
                lower_bound=0))
            votes[vote_permutations[permutation_index-1]] = num_votes
            str_vote_permutations.pop(permutation_index)
            vote_permutations.pop(permutation_index-1)
            permutation_index = str_vote_permutations.index(
                self.prompt_choices(
                    "Which permutations have votes >", str_vote_permutations)
            )

        # Set Inputs
        self.inputs = dict()
        self.inputs['candidates'] = candidates
        self.inputs['votes'] = votes
