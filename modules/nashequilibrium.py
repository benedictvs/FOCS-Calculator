from abstractclasses import solver, solver_model

"""
The Nash equilibrium solver takes a payoff matrix from game theory,
then it solves for a nash equilibrium, if one exists.
"""


# ————————————————————————————————————————————————
# NASH EQUILIBRIUM SOLVER CLASS
# ————————————————————————————————————————————————


class nash_equilibrium_solver(solver):
    def format_payoff_matrix(
        self,
        payoff_matrix: list,
        player_1_strategies: list,
        player_2_strategies: list,
    ) -> str:
        """
        This is a helper function that turns a payoff matrix and available
        strategies into ASCII art of a payoff matrix
        """
        ret = "\t    Player 1\n"
        ret += "\t          " + player_1_strategies[0] + "            "
        for j in range(1, len(payoff_matrix[0])):
            ret += player_1_strategies[j] + "            "
        ret += "\n"
        ret += "\t    +------------+"
        for j in range(1, len(payoff_matrix[0])):
            ret += "------------+"
        ret += "\n"
        ret += "Player 2  " + str(player_2_strategies[0]) + " |"
        for j in range(len(payoff_matrix[0])):
            ret += (
                "{:>5g}, {:<5g}".format(
                    payoff_matrix[0][j][0], payoff_matrix[0][j][1]
                )
                + "|"
            )
        ret += "\n"
        for i in range(1, len(payoff_matrix)):
            ret += "\t    +------------+"
            for j in range(1, len(payoff_matrix[0])):
                ret += "------------+"
            ret += "\n"
            ret += (
                "\t  "
                + player_2_strategies[i]
                + " |"
                + "{:>5g}, {:<5g}".format(
                    payoff_matrix[i][0][0], payoff_matrix[i][0][1]
                )
                + "|"
            )
            for j in range(1, len(payoff_matrix[i])):
                ret += (
                    "{:>5g}, {:<5g}".format(
                        payoff_matrix[i][j][0], payoff_matrix[i][j][1]
                    )
                    + "|"
                )
            ret += "\n"
        ret += "\t    +------------+"
        for j in range(1, len(payoff_matrix[0])):
            ret += "------------+"
        ret += "\n"
        return ret

    def prompt_inputs(self) -> None:
        player_1_strategies = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
        ]
        player_2_strategies = [
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]

        num_strategies_1 = self.prompt_integer(
            "Please enter the number of strategies for player 1 (2-13) > ",
            2,
            13,
        )
        num_strategies_2 = self.prompt_integer(
            "Please enter the number of strategies for player 2 (2-13) > ",
            2,
            13,
        )

        player_1_strategies = player_1_strategies[:num_strategies_1]
        player_2_strategies = player_2_strategies[:num_strategies_2]

        payoff_matrix = [
            [(0, 0) for i in range(num_strategies_1)]
            for j in range(num_strategies_2)
        ]

        print(
            self.format_payoff_matrix(
                payoff_matrix, player_1_strategies, player_2_strategies
            )
        )
        for i in range(num_strategies_2):
            for j in range(num_strategies_1):
                player_1_payoff = self.prompt_float(
                    "Please enter the payoff value for Player "
                    + str(1)
                    + " in cell "
                    + str(player_1_strategies[j])
                    + ", "
                    + str(player_2_strategies[i])
                    + " of the payoff matrix > "
                )
                player_2_payoff = self.prompt_float(
                    "Please enter the payoff value for Player "
                    + str(2)
                    + " in cell "
                    + str(player_1_strategies[j])
                    + ", "
                    + str(player_2_strategies[i])
                    + " of the payoff matrix > "
                )
                payoff_matrix[i][j] = (player_2_payoff, player_1_payoff)
                print(
                    self.format_payoff_matrix(
                        payoff_matrix, player_1_strategies, player_2_strategies
                    )
                )

        # Set inputs
        self.inputs["payoff_matrix"] = payoff_matrix
        self.inputs["player_1_strategies"] = player_1_strategies
        self.inputs["player_2_strategies"] = player_2_strategies
        self.inputs["format_payoff_matrix"] = self.format_payoff_matrix


# ————————————————————————————————————————————————
# NASH EQUILIBRIUM MODEL CLASS
# ————————————————————————————————————————————————


class nash_equilibrium_model(solver_model):
    def __init__(self, **inputs) -> None:
        super().__init__(**inputs)
        self.format_payoff_matrix = self.inputs["format_payoff_matrix"]

    def solve(self) -> None:
        payoff_matrix = self.inputs["payoff_matrix"]
        player_1_strategies = self.inputs["player_1_strategies"]
        player_2_strategies = self.inputs["player_2_strategies"]

        self.ans, self.work = self.nash(
            payoff_matrix, player_1_strategies, player_2_strategies
        )

    def nash(
        self,
        payoff_matrix: list,
        player_1_strategies: list,
        player_2_strategies: list,
    ) -> tuple:
        """
        Takes a payoff matrix from game theory and the available strategies for
        both players. Solves for the Nash equilibrium
        """
        work = ""

        no_dominant_exists = False
        while not no_dominant_exists and not (
            len(player_1_strategies) == 1 and len(player_2_strategies) == 1
        ):
            is_break = False
            for i in range(len(payoff_matrix)):
                for j in range(len(payoff_matrix)):
                    if (
                        i != j
                        and i < len(payoff_matrix)
                        and j < len(payoff_matrix)
                    ):
                        is_greater = False
                        for k in range(len(payoff_matrix[0])):
                            if float(payoff_matrix[i][k][0]) >= float(
                                payoff_matrix[j][k][0]
                            ):
                                is_greater = True
                            if is_greater:
                                break
                        if not is_greater:
                            work += (
                                "Player 2's Strategy "
                                + str(player_2_strategies[j])
                                + " dominates strategy "
                                + str(player_2_strategies[i])
                                + "\n"
                            )
                            payoff_matrix.pop(i)
                            player_2_strategies.pop(i)
                            is_break = True
                            work += self.format_payoff_matrix(
                                payoff_matrix,
                                player_1_strategies,
                                player_2_strategies,
                            )
                            work += "\n"
                            break
                    if is_break:
                        break

            if not is_break:
                no_dominant_exists = True
            else:
                no_dominant_exists = False

            is_break = False
            for i in range(len(payoff_matrix[0])):
                for j in range(len(payoff_matrix[0])):
                    if (
                        i != j
                        and i < len(payoff_matrix[0])
                        and j < len(payoff_matrix[0])
                    ):
                        is_greater = False
                        for k in range(len(payoff_matrix)):
                            if float(payoff_matrix[k][i][1]) >= float(
                                payoff_matrix[k][j][1]
                            ):
                                is_greater = True
                            if is_greater:
                                break
                        if not is_greater:
                            work += (
                                "Player 1's Strategy "
                                + str(player_1_strategies[j])
                                + " dominates strategy "
                                + str(player_1_strategies[i])
                                + "\n"
                            )
                            for index in range(len(payoff_matrix)):
                                payoff_matrix[index].pop(i)
                            player_1_strategies.pop(i)
                            work += self.format_payoff_matrix(
                                payoff_matrix,
                                player_1_strategies,
                                player_2_strategies,
                            )
                            work += "\n"
                            is_break = True
                            break
                    if not is_break:
                        no_dominant_exists = True
                    else:
                        no_dominant_exists = False

            if is_break:
                no_dominant_exists = False

        if not (
            len(player_1_strategies) == 1 and len(player_2_strategies) == 1
        ):
            ans = (
                "There is no Nash equilibrium, since at least one player has"
                + " multiple viable strategies.\n"
            )
            work += ans
            work += self.format_payoff_matrix(
                payoff_matrix, player_1_strategies, player_2_strategies
            )
        else:
            ans = (
                "This is the Nash equilibrium of the entered payoff matrix,"
                + " calculated by eliminating dominanted strategies.\n"
            )
            ans += self.format_payoff_matrix(
                payoff_matrix, player_1_strategies, player_2_strategies
            )
            work += ans
        return ans, work
