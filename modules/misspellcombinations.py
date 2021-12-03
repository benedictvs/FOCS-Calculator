from abstractclasses import solver, solver_model

"""
Misspell combinations solves for how many ways one can misspell a word
"""

# ————————————————————————————————————————————————
# MISSPELL COMBINATIONS SOLVER CLASS
# ————————————————————————————————————————————————


class misspell_combinations_solver(solver):
    def prompt_inputs(self) -> None:
        n_arg = self.prompt_string(
            "How many ways can you misspell the word: (Enter word)"
        )
        k_arg = self.prompt_integer(
            "Length of the word you want to misspell: ", lower_bound=1 
        )

        # Set inputs
        self.inputs["n_arg"] = n_arg
        self.inputs["k_arg"] = k_arg
        self.inputs["MAX_CHAR"] = 26


# ————————————————————————————————————————————————
# MISSPELL COMBINATIONS MODEL CLASS
# ————————————————————————————————————————————————


class mispell_combinations_model(solver_model):
    def __init__(self, **inputs) -> None:
        super().__init__(**inputs)
        self.MAX_CHAR = self.inputs["MAX_CHAR"]

    def solve(self) -> None:
        n = self.inputs["n_arg"].lower()
        k = self.inputs["k_arg"]

        self.ans = str(self.misspell(n, k))
        self.work = self.misspellwork(n, k)

    def factorial(self, j: int) -> int:
        """
        Utility function to find factorial of n
        """
        fact = 1
        for i in range(2, j + 1):
            fact = fact * i
        return fact
    
   
    
    def countDis(self, str:str) -> int:
 
        # Stores all distinct characters
        s = set(str)
 
        # Return the size of the set
        return len(s)

    def misspell(self, n: str, k: int) -> str:
        """
        Finds the maximum possible misspell combinations
        """
        s=n
        #for errors
        if(k > len(n)):
            return "error k is larger than length of n \n",
        #standard misspell
        elif(k == len(n)):
            length = len(n)
            freq = [0] * self.MAX_CHAR

            # finding frequency of all the lower
            # case alphabet and storing them in
            # array of integer
            for i in range(0, length):
                if n[i] >= "a":
                    freq[(ord)(n[i]) - 97] = freq[(ord)(n[i]) - 97] + 1

            # finding factorial of number of
            # appearances and multiplying them
            # since they are repeating alphabets
            fact = 1
            for i in range(0, self.MAX_CHAR):
                fact = fact * self.factorial(freq[i])

            # finding factorial of size of string
            # and dividing it by factorial found
            # after multiplying
            return "For the word {} there are {} misspellings\n".format(s, str(self.factorial(length) / fact - 1) )
        #standard permutation formula
        else: 
            length = self.countDis(n)
            if(k>length): return "error not enough letters"
            else:
                factlen = self.factorial(length)
                denom = length-k 
                denom = self.factorial(denom)
                denom = denom * self.factorial(k)

                return "For the word {} there are {} substring which are of length {}\n".format(s, factlen / denom, k)

        return "\n"


    def misspellwork(self, n: str, k: int) -> str:
        """
        Shows the work necessary to find the maximum mispell combinations.
        """
        
        steps = "For permutations or misspelling of a word the equation is: \n"
        steps += "P = n!/(a!b!c!...z!) - 1, where n is the number of letters in the word and a,b,c,..,z are the number of times each letter occurs \n"
        steps += "A word with no repeats will have P=n!-1 (All the variables in the denominater are either 0! or 1! which results in the denominator =1)\n"
        steps += ("Ex. cake has P=4!-1 which is 24-1=23, we subtract 1 at the end for the correct spelling of cake.")
        steps += "Ex with repeats: success P=4!/(2!1!3!1!) - 1, the length is 7 and there are (2c,1e,3s and 1u)\n"
        steps += "success P=5040/(12) - 1 = 420-1 = 419\n"
        steps += "For permutations or misspellings of a word shorter than the word recall permutation formula:\n" 
        steps += "m!/((m-k)!)(k!) where m is the number of unique letters in the word and k is the target length.\n"
        return steps
