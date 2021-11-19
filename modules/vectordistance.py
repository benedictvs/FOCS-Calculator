import math as m

from questionary import prompt, print

from abstractclasses import solver, solver_model

"""
Vector Distance solves for the distance between two points in 2 or 3
dimensional space. 
"""

# ————————————————————————————————————————————————
# VECTOR DISTANCE SOLVER CLASS
# ————————————————————————————————————————————————


class vector_distance_solver(solver):
    def prompt_inputs(self) -> None:
        x0_arg = self.prompt_float("Please enter the x value of the first point > ")
        y0_arg = self.prompt_float("Please enter the y value of the first point > ")
        z0_arg = self.prompt_float(
            "Please enter the z value of the first point (enter 0 if 2D) "
        )
        x1_arg = self.prompt_float("Please enter the x value of the second point > ")
        y1_arg = self.prompt_float("Please enter the y value of the second point > ")
        z1_arg = self.prompt_float(
            "Please enter the z value of the second point (enter 0 if 2D) "
        )

        # Set inputs
        self.inputs["x0_arg"] = x0_arg
        self.inputs["y0_arg"] = y0_arg
        self.inputs["z0_arg"] = z0_arg
        self.inputs["x1_arg"] = x1_arg
        self.inputs["y1_arg"] = y1_arg
        self.inputs["z1_arg"] = z1_arg


# ————————————————————————————————————————————————
# VECTOR DISTANCE MODEL CLASS
# ————————————————————————————————————————————————


class vector_distance_model(solver_model):
    def solve(self) -> None:
        x0 = self.inputs["x0_arg"]
        y0 = self.inputs["y0_arg"]
        z0 = self.inputs["z0_arg"]
        x1 = self.inputs["x1_arg"]
        y1 = self.inputs["y1_arg"]
        z1 = self.inputs["z1_arg"]
        self.ans = self.distance(x0, y0, z0, x1, y1, z1)
        self.work = self.distancework(x0, y0, z0, x1, y1, z1, "")

    def distance(self, x0: int, y0: int, z0: int, x1: int, y1: int, z1: int) -> float:
        """
        Takes xyz coordinates of two points and solves for their vector
        distance
        """
        squared = (x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2
        return m.sqrt(squared)

    def distancework(
        self, x0: int, y0: int, z0: int, x1: int, y1: int, z1: int, v: str
    ) -> str:
        """
        Takes xyz coordinates of two points and shows how to solve for
        vector distance
        """
        v += "x squared is {}.".format((x1 - x0) ** 2) + "\n"
        v += "y squared is {}.".format((y1 - y0) ** 2) + "\n"
        v += "z squared is {}.".format((z1 - z0) ** 2) + "\n"
        squared = (x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2
        v += (
            "add x squared, y squared, and z squared together to get {}.".format(
                squared
            )
            + "\n"
        )
        v += (
            "take the square root to get the "
            + "answer: {}".format(m.sqrt(squared))
            + "\n"
        )
        return v
