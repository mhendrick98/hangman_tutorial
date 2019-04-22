import random

# The class that represents the user who is playing the game
class Player:
    def __init__(self, name): # Our constructor
        self.name = name # The name of a player
        self.mistakes = 0 # Keep track of the letters the user has guessed so far
        self.total_mistakes_allowed = 3 # Number of mistakes the user is allowed to make before the game ends
        self.letters_guessed = [] # Keep track of the letters the user has guessed so far
        self.user_picks = [] # Keep track of the word the user can see while they are guessing


# The class that holds the information needed to play the game
class Game:
    def __init__(self):
        self.words = ["jack", "computer", "science", "michael", "apple", "windows", "linux", "operating", "system"] # Possible words that could be guessed
        self.answer = random.choice(self.words) # The word the user is trying to guess
        self.player = None # The player who is playing the game (gets replaced with a real player during the driver code)


    # Checks to see if the user has guessed the right word (returns true/false)
    def check_word(self, guess):
        return guess == self.answer # Returns true if it's a match or false otherwise


    # Checks to see if the user has guessed a letter that's in the word (returns updated user_picks)
    def check_letter(self, guess):
        if guess in self.player.letters_guessed: # Checks to see if the player has already guessed the letter
            print("You already guessed this letter!")
            return self.player.user_picks
        if guess in self.answer: # Checks to see if the user guessed a letter that's in the word
            for i in range(len(list(self.answer))): # This loops updates what the user can see with the guessed words
                if(self.answer[i] == guess or self.player.user_picks[i] != ""):
                    self.player.user_picks[i] = self.answer[i]
            self.player.letters_guessed.append(guess) # Adds the letter to the guessed list and sorts it for readability
            self.player.letters_guessed.sort()
            return self.player.user_picks
        else: # If it's not in the word, we should still add it to the guess list.
            self.player.letters_guessed.append(guess)
            self.player.letters_guessed.sort()
        return self.player.user_picks


    # Removes a life from the player (returns true / false)
    def remove_a_life(self):
        self.player.mistakes += 1
        if self.player.mistakes >= self.player.total_mistakes_allowed:
            print("Game over! You're out of lives! The word was", self.answer)
            return True
        print("Wrong! You've lost a life! You have", self.player.total_mistakes_allowed - self.player.mistakes,"lives left!\n")
        return False


    def print_nice(self): # This function makes a nice display for the user
        temp = ""
        for i in range(len(self.player.user_picks)):
            if (self.player.user_picks[i] == ""):
                temp += " _ "
            else:
                temp += self.player.user_picks[i]
        return temp


# function to start the game
def play_game():
    name = input("Hello! Welcome to Hangman! What is your name: ") # Gets the name of the player
    game = Game() # Creates a new game
    game.player = Player(name) # Creates a player for the game
    game.player.user_picks = ["" for x in game.answer] # Creates the right amount of spaces for the user to guess
    print("We've chosen the word " + game.player.name + "! Let us begin the game! \n")

    while(True): # This repeats until the game ends
        print("Letters guessed so far", game.player.letters_guessed, "\n") # Some print statements to let the user know where they are in the game.
        print("Current status of the word is", game.print_nice(), "\n")
        type_of_move = input("Would you like to guess the word (1) or guess a letter (2): ")
        if type_of_move == "1":
            guess = input("Type in your guess: ")
            if game.check_word(guess): # Uses the function above to check for a victory
                print("You guessed the word! You win!\n")
                return
            else:
                if game.remove_a_life(): # Made the wrong move, so we delete a life and possibly end the game
                    return

        elif type_of_move == "2":
            guess = input("Type in your letter: ")
            current_picks = [x for x in game.player.user_picks] # Creates a deep copy of the current picks; we'll use this to validate a correct guess
            new_user_picks = game.check_letter(guess) # Use the function above to validate the guess, and store the result
            if new_user_picks == current_picks: # If the deep copy equals the new list, that means nothing changed and they made a bad guess!
                if game.remove_a_life(): # Made the wrong move, so we delete a life and possibly end the game
                    return
            else:
                print("Nice work! That letter is in the word!\n")
        else:
            print("Please type in 1 or 2")


play_game() # Run the code
