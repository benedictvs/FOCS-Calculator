# FOCS Calculator
FOCS Calculator is a command line application designed for solving niche mathematical problems, specifically those encountered in discrete mathematics. This powerful tool allows you to see the works and steps behind your answer, giving you insight and unserstanding you may not have gotten from the class.

## Installation Guide
Installing FOCS Calculator is quite simple. There are very few requirements.

1. Clone the repository locally onto your machine
2. Open up your terminal and enter the command `python --version`. If you do not have at least version 3.9.6, or you do not have Python installed. Please update and install that now.
3. Navigate to the directory that you installed FOCS Calculator to, and run the command `pip install -r requirements.txt`
    1. If pip install fails, run `pip install [package]` on all of the packages listed on requirements.txt. Ideally, you should be updated to the latest version of pip and the latest versions of those packages. Not being updated is unlikely to break something, but do so at your own risk. 
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
5. Add your new instantiated module object into the arguments of main()

## Coding Standards
Follow Python's PEP8 standard found [here](https://www.python.org/dev/peps/pep-0008/)
Used python formatter black to format most of code, found [here](https://pypi.org/project/black/)
Used python linter flake8 to lint all of the codebase, foun [here](https://pypi.org/project/flake8/)

## Attributions
This project makes use of code from the pylambdac python lambda calculus interpreter to power the lambda calculus module. This code is licensed using the Apache License 2.0. The proper attributions are present on each file, as ATTRIBUTIONS.md