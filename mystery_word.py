#remember!
# - import random module
# - open .txt file with syntax
# - words from .txt file into list of strings
# - indicate mystery word letters as symbol, _ or - or * , ie let them know how long the word is
# - ask for user guess | user gets one guess per round message
# - limit guesses to 8
#   - if more than one letter is guessed, invalid message to user w instructions to try again
#   - if previous letter is guessed, display error message to user & does not count towards 8 guesses
# - reveal to user if guessed letter is in word | replace symbol w correct letter
# - keep track of user guesses | show user how many guesses are left
# - user loses round only if guess is incorrect
# - display letters not yet guessed
# - reveal mystery word after 8th incorrect guess
#   - you lose message
# - provide user w play again message at end of game

# need
# - global variables
# - empty index
# - empty strings
# - empty guesses
# - empty misses




import random

def play_game():
    print("hello!")

    file = open(words.txt)
    words = file.read().upper().split()
    word = word.replace("\n", "")
    print("words")
    

# global mystery_words
# mystery_words = ''

# global mystery_words_list
# mystery_words_list = list(mystery_words)

# global mystery_words_underscores
# mystery_words_underscores = []
# for char in mystery_words_list:
#     mystery_words_underscores.append("_")


# def random_word_generator():
    # file = open("words.txt")
    # word_file = file.read()
    # word_file_list = (word_file.upper()).split()
    # return random.choice(word_file_list)









    
    # mystery_words = file.read().upper().split()
    # mystery_words = choice(words)
    # mystery_words = word.replace("\n", "")
    # mystery_words_list = []
    
        # return random.choice(mystery_words_list)


if __name__ == "__main__":
    play_game()