# FOCS Calculator
FOCS Calculator is a command line application designed for solving niche mathematical problems, specifically those encountered in discrete mathematics. This powerful tool allows you to see the works and steps behind your answer, giving you insight and unserstanding you may not have gotten from the class.

## Installation Guide
Installing FOCS Calculator is quite simple. There are very few requirements.

1. Clone the repository locally onto your machine
2. Open up your terminal and enter the command `python --version`. If you do not have at least version 3.9.6, or you do not have Python installed. Please update and install that now.
3. Navigate to the directory that you installed FOCS Calculator to, and run the command `pip freeze > requirements.txt`
4. Finally, run the command `python main.py` and you should be good to go!

## Development Guide
To create a new module, do the following: 

1. Create a new file in the modules folder, following the naming conventions of the other files
2. Create two new classes in that file that inherit from the python abstract basic classes in abstractclasses.py
    1. A solver class inheriting from solver, that implements prompt_inputs
    2. A model class inheriting from solver_model, that implements solve
3. Import your new classes into main.py
4. Instantiate your solver class at the bottom of main.py, passing in the following arguments
    1. The name of your module
    2. Your module class