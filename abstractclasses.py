from abc import ABC, abstractmethod
from typing import Callable

from questionary import prompt, print

# ————————————————————————————————————————————————
# SOLVER MODEL INTERFACE
# ————————————————————————————————————————————————


class solver_model(ABC):
    def __init__(self, **inputs) -> None:
        self.inputs = inputs
        self.ans = None
        self.work = None

    def __call__(self) -> tuple:
        """
        Call the solver_model like a function for the intended execution order
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
        self.inputs = dict()
        self.ans = None
        self.work = None

    def __str__(self) -> str:
        return self.name

    def __call__(self) -> None:
        """
        Call the solver like a function to run its intended exection order
        """
        self.prompt_inputs()
        if not self.inputs:
            raise ValueError("self.inputs not set in prompt_inputs")
        _model = self.model(**self.inputs)
        self.ans, self.work = _model()
        self.prompt_outputs()

    def prompt_outputs(self) -> None:
        print("\nYour answers:\n{}".format(self.ans),
              style="bold italic fg:yellow")
        print("Work:\n{}".format(self.work),
              style="bold italic fg:yellow")
        input("\nPlease hit enter when you are finished.")

    @abstractmethod
    def prompt_inputs(self) -> None:
        """
        This method should prompt the user for all the necessary inputs. Some
        useful helper functions for common input prompts are provided below,
        but developers can write their own input prompts. Once inputs are
        collected, write them to self.inputs
        """
        pass

    def prompt_integer(
            self, message_text: str, lower_bound: int = None,
            upper_bound: int = None) -> int:
        """
        Helper function to prompt for integer

        Enter the message text you want to be displayed to the user.
        Additionally, enter the upper/lower bounds (using >= and <=) of the
        integer (if there are any).
        """
        questions = [
            {
                "qmark": self.name,
                "type": "text",
                "name": "integer",
                "message": message_text,
                "validate": lambda val: val.isdigit()
                and (True if lower_bound is None else int(val) >= lower_bound)
                and (True if upper_bound is None else int(val) <= upper_bound),
            },
        ]
        return int(prompt(questions)["integer"])

    def prompt_integer_custom(
        self, message_text: str, validate: Callable = None, *args
    ) -> int:
        """
        Helper function to prompt for integer, with custom validation

        Enter the message text you want to be displayed to the user.
        Additionally, you can add optional validation logic, using
        the validate function, and args to pass into it. The function should
        work as follows, where val is the value entered by the user:
            def validate(val, args) -> bool
        """
        questions = [
            {
                "qmark": self.name,
                "type": "text",
                "name": "integer",
                "message": message_text,
            },
        ]
        return int(
            prompt(
                questions,
                validate=lambda val: val.isdigit()
                and (validate(val, args) if validate else True),
            )["integer"]
        )

    def is_float(self, a: str) -> bool:
        """
        Takes a string and determines whether it can be converted to
        a float
        """
        try:
            float(a)
        except(ValueError):
            return False
        return True

    def prompt_float(
            self, message_text: str, lower_bound: int = None,
            upper_bound: int = None) -> float:
        """
        Helper function to prompt for float

        Enter the message text you want to be displayed to the user.
        Additionally, enter the upper/lower bounds (using >= and <=) of the
        integer (if there are any).
        """
        questions = [
            {
                "qmark": self.name,
                "type": "text",
                "name": "float",
                "message": message_text,
                "validate": lambda val: self.is_float(val)
                and (True if lower_bound is None else float(val) >= lower_bound)
                and (True if upper_bound is None else float(val) <= upper_bound),
            },
        ]
        return float(prompt(questions)["float"])

    def prompt_float_custom(
        self, message_text: str, validate: Callable = None, *args
    ) -> float:
        """
        Helper function to prompt for float, with custom validation

        Enter the message text you want to be displayed to the user.
        Additionally, you can add optional validation logic, using
        the validate function, and args to pass into it. The function should
        work as follows, where val is the value entered by the user:
            def validate(val, args) -> bool
        """
        questions = [
            {
                "qmark": self.name,
                "type": "text",
                "name": "float",
                "message": message_text,
            },
        ]
        return float(
            prompt(
                questions,
                validate=lambda val: self.is_float(val)
                and (validate(val, args) if validate else True),
            )["float"]
        )

    def prompt_string(self, message_text: str, validate: Callable = None,
                      *args) -> str:
        """
        Helper function to prompt for string

        Enter the message text you want to be displayed to the user.
        Additionally, you can add optional validation logic, using
        the validate function, and args to pass into it. The function should
        work as follows, where val is the value entered by the user:
            def validate(val, *args) -> bool
        """
        questions = [
            {
                "qmark": self.name,
                "type": "text",
                "name": "string",
                "message": message_text,
            },
        ]
        return str(
            prompt(
                questions,
                validate=lambda val: val.isalpha()
                and (validate(val, args) if validate else True),
            )["string"]
        )

    def prompt_choices(self, message_text: str, choices: list) -> any:
        """
        Helper function to prompt for a choice in a list

        Enter the message text you want to be displayed to the user.
        Enter the list of choices for the user
        """
        questions = [
            {
                "qmark": self.name,
                "type": "select",
                "name": "choice",
                "message": message_text,
                "choices": choices,
            },
        ]
        return prompt(questions)["choice"]
