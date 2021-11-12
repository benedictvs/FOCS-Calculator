from abc import ABC, abstractmethod

# ————————————————————————————————————————————————
# SOLVER INTERFACE
# ————————————————————————————————————————————————


class solver(ABC):
    def __init__(self, name: str, model: object) -> None:
        self.name = name
        self.model = model
        self.inputs: tuple = None

    def __str__(self) -> str:
        return self.name

    def __call__(self) -> tuple:
        self.prompt_inputs()
        ans, work = self.model(self.inputs)
        return ans, work

    @abstractmethod
    def prompt_inputs(self) -> None:
        """
        This method should prompt the user for all the necessary inputs. Some 
        useful helper functions for common input prompts are provided below, 
        but developers can write their own input prompts. Once inputs are 
        collected, write them to self.inputs
        """
        pass


# ————————————————————————————————————————————————
# SOLVER MODEL INTERFACE
# ————————————————————————————————————————————————


class solver_model(ABC):
    def __init__(self, *inputs) -> None:
        self.inputs = inputs
        self.ans: str = None
        self.work: str = None

    @abstractmethod
    def solve(self) -> None:
        """
        All module logic belongs here. Can create additional helper functions 
        if necessary. Write answer to self.ans and work to self.work
        """
        pass
