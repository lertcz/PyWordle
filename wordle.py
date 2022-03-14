from words import wordlist
from random import choice
from termcolor import colored

HEADER = '\033[95m'
OKGREEN = '\033[92m'

class Wordle:
    def __init__(self, hint:bool=False) -> None:
        self.word = choice(wordlist)
        self.board = [["_" for _ in range(5)] for _ in range(6)]
        
        if hint:
            print(self.word)

    
    def returnBoard(self):
        for row in self.board:
            for char in row:
                print(char, end="")
            print()
    
    def game(self):
        guessNumber = 0
        while True:
            self.returnBoard()
            guess = input(">")
            if guess in self.words:
                for i in range(5):
                    # the letter is in a correct spot
                    if guess[i] == self.word[i]:
                        self.board[guessNumber][i] = colored(guess[i].upper(), "green")
                    # the letter is in the word but on other spot
                    elif guess[i] in self.word:
                        self.board[guessNumber][i] = colored(guess[i].upper(), "yellow")
                    # not in the word
                    else:
                        self.board[guessNumber][i] = guess[i].upper()
                guessNumber += 1

                # if you guessed the word or you are out of guessed end the loop
                if guess == self.word or guessNumber == 6:
                    print("\n") # newline
                    break

            else:
                print("not a legal word")
                print("\n") # newline
                self.game()

            print("\n") # newline

        self.returnBoard() # the final board


wordle = Wordle(hint=False)
wordle.game()