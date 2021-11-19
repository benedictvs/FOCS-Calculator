from abstractclasses import solver, solver_model


class conditional_probability_solver(solver):
    def prompt_inputs(self) -> None:
        choices = ["Probability of A", "Probability of B"]
        probabilities = dict()
        for c in choices:
            probabilities[c] = 0.0
        for _ in range(2):
            choice = self.prompt_choices(
                "Given two events A and B enter the probability for one of the"
                + " following > ",
                choices,
            )
            prob = self.prompt_float(
                "Enter the probabilty (0.0 - 1.0) > ", 0.0, 1.0
            )
            probabilities[choice] = prob

        # set inputs
        self.inputs["probabilities"] = probabilities


class conditional_probability_model(solver_model):
    def solve(self) -> None:
        work = ""
        new_probabilities = [
            "Probability of A",  # 0
            "Probability of B",  # 1
            "Probability of not A",  # 2
            "Probability of not B",  # 3
            "Probability of A and B",  # 4
            "Probability A or B",  # 5
            "Probability A xor B",  # 6
            "Probability of not A and Not B",  # 7
        ]
        probabilities = self.inputs["probabilities"]
        probabilities[new_probabilities[2]] = (
            1 - probabilities[new_probabilities[0]]
        )
        work += new_probabilities[2]
        work += "= 1 - {} = {}".format(
            new_probabilities[0], probabilities[new_probabilities[2]]
        )
        probabilities["Probability of not B"] = (
            1 - probabilities["Probability of B"]
        )

        ans = ""
        for i in range(len(new_probabilities)):
            ans += "{} = {}\n".format(
                new_probabilities[i], probabilities[new_probabilities[i]]
            )
