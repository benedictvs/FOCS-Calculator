from abc import ABC, abstractmethod

from questionary import prompt, print

# ————————————————————————————————————————————————
# SOLVER MODEL INTERFACE
# ————————————————————————————————————————————————


class solver_model(ABC):
    def __init__(self, *inputs) -> None:
        self.inputs = inputs
        self.ans: str = None
        self.work: str = None

    def __call__(self) -> tuple:
        """
        Call the solver_model like a function for the intended execution order.
        Called by the __call__ function in the solver class. 
        """
        self.solve()
        if self.ans is None:
            raise ValueError("solve did not set self.ans")
        if self.work is None:
            raise ValueError("solve did not set self.work")
        return self.ans, self.work

    @abstractmethod
    def solve(self) -> None:
        """
        All module logic belongs here. Can create additional helper functions 
        if necessary. Write answer to self.ans and work to self.work
        """
        pass

# ————————————————————————————————————————————————
# SOLVER INTERFACE
# ————————————————————————————————————————————————


class solver(ABC):
    def __init__(self, name: str, model: solver_model) -> None:
        self.name = name
        self.model = model
        self.inputs: tuple = None
        self.ans : str = None
        self.work : str = None

    def __str__(self) -> str:
        return self.name

    def __call__(self) -> None:
        """
        Call the solver like a function to run its intended exection order
        """
        self.prompt_inputs()
        if self.inputs is None:
            raise ValueError("self.inputs not set in prompt_inputs")
        _model = self.model(self.inputs)
        self.ans, self.work = _model()
        self.prompt_outputs()

    def prompt_outputs(self) -> None:
        print('\nYour answers:\n{}'.format(self.ans),
          style="bold italic fg:yellow")
        print('Work:\n{}'.format(self.work), style="bold italic fg:yellow")
        input('\nPlease hit enter when you are finished.')
        
    @abstractmethod
    def prompt_inputs(self) -> None:
        """
        This method should prompt the user for all the necessary inputs. Some 
        useful helper functions for common input prompts are provided below, 
        but developers can write their own input prompts. Once inputs are 
        collected, write them to self.inputs
        """
        pass

    def prompt_integer(self, message_text: str, lower_bound: int = None, upper_bound: int = None) -> int:
        """
        Enter the message text you want to be displayed to the user, as well as 
        the qmark, which is what you want the interface to identify itself as.  
        Additionally, enter the upper/lower bounds (using >= and <=) of the 
        integer (if there are any).
        """
        questions = [
            {
                "qmark": self.name,
                "type": "text",
                "name": "integer",
                "message": message_text,
                "validate": lambda val: val.isdigit() and\
                     (True if lower_bound is None else int(val) >= lower_bound) and\
                          (True if upper_bound is None else int(val) <= upper_bound),
            },
        ]
        return int(prompt(questions)['integer'])