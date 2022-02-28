import string
from random import choice

from pyparsing import empty

def play_game():
    import random
print("\n***Wurdle***\n")
print("You have 8 attempts to pretend that this is the real Wordle. Type quit to end the game.\n\n\n")
import random

wurds = []

underscores = []
end_game = False
guess_turns = 8
incorrect_guesses = []
global wurdle_wurds


with open('words.txt') as file:
    strings = file.readlines()
    for string in strings:
        wurds.append(string)
    wurdle_wurds = random.choice(wurds)
    wurdle_wurds = wurdle_wurds.replace("\n", "")

    wurdle_display = range(len(wurdle_wurds))
    for num in wurdle_display:
        underscores.append('_')
    underscores = "".join(underscores)

    print("_".join(underscores))
    wurdle_display = ["_"] * len(wurdle_wurds)
    print(f"Your word is {len(wurdle_wurds)} letters long.")


def wurd_display(wurds,guesses):
    wurdle_display = []
    for letter in wurds:
        if letter in guesses:
            wurdle_display.append(letter)
        else:
            wurdle_display.append('_')
        wurdle_display = ' '.join(wurdle_display)
        wurdle_display = wurdle_display.upper()
        return wurdle_display


def complete_wurd(wurds, guesses):
    wurdle = wurd_display(wurds, guesses)
    

















# while guess_turns > 0:
#     if "_" not in wurdle_display:
#         print("You win!")
#         quit()

#     guess = input("Guess the letter: ").casefold()
#     i = 0 
#     if len(guess) != 1:
#         print("One character plz")
#     if guess in wurdle_wurds:
#         for letter in wurdle_wurds:
#             if letter == guess:
#                 wurdle_display[i] = guessed_letters
#                 print("nice guess")
#             i += 1
#         print(wurdle_display)
#     if guess not in wurdle_wurds:
#         for letter in wurdle_wurds:
#             if letter != guess:
#                 guess = incorrect_guesses
#                 incorrect_guesses.append(guess)
#                 print("nope!")
#         print(wurdle_display)


    # guess not in wurdle_wurds[i] and guess_turns > 8:
    #     end_game == True
    #     print(f"You lose! The word was {wurdle_wurds}")



    # else:
    #     guess_turns = guess_turns - 1
    #     incorrect_guesses.append(wurdle_wurds)
    #     print(f"You have {guess_turns} of 8 guesses left. What letter do you guess?")
    # # print(f"You lose! The word was {wurdle_wurds}")








    # for index in range(len(wurdle_wurds)):
    #     if wurdle_wurds[index] == guess:
    #         underscores = underscores[0:index] + guess + underscores[index+1:]
    #         guess + underscores[index+1:]
    # print(underscores)



    # if guess in wurdle_wurds:
    #     print("Correct! Great guess.")
    #     guessed_letters.append(guess)
    #     guess = input('Guess again... ')

    # else: 
    #     guess != wurdle_wurds
    #     guess = input('Guess again... ')
    #     guess_count += 1
    #     # print("Number of guesses made: " + (str(guess_count)))
    #     # guessed_letters.append(user_input)
    #     player_letter = input(f"You have made {guess_count} of 8 guesses left. What letter do you guess?").upper()  # uppercase the users input
    #     guess_list.append(player_letter)
    #     guessed_letters += f" {player_letter}, "
    #     print(guessed_letters)   
    #     if guess_count >= 8:
    #         end_game =True
    #         print(str(wurdle_wurds))








# guess = input('Guess a letter: ').upper()
# while guess != 'Quit' and end_game == False:
#     for index in range(len(wurdle_wurds)):
#         if wurdle_wurds[index] == guess:
#             underscores = underscores[0:index] + guess + underscores[index+1:]
#     print(underscores)
#     guess = input("LOL no.")
    
    
    
# while guess_turns > 0:
#     guess = input('Guess a letter: ').upper()
#     guessed_letters.append(guess)
    
#     if guess != wurdle_wurds:
        
    # i = 0
    # if len(guess) != 1:
    #     print("One letter only, come on")
    # if guess in wurdle_wurds:
    #     for letter in wurdle_wurds:
    #         if letter == guess:
    #             wurdle_display[i] = letter
    #             print("LOL no")
    #         i += 1
    #     print(wurdle_display)
    # elif "_" not in wurdle_display:
    #     print("ya wun wurdle!")
    #     quit()
    # else:
    #     incorrect_guesses.append(guess)
    #     guess_turns = guess_turns - 1
    # print(incorrect_guesses)
    # print(f"You have {guess_turns} of 8 guesses left. What letter do you guess?")
        # print(f"You lose! The word was {wurdle_wurds}")




# with open('words.txt') as file:
#     strings = file.readlines()
#     for string in strings:
#         wurdle.append(string)
#     wurdle_wurds = random.choice(wurdle)
#     wurdle_wurds = wurdle_wurds.replace("\n", "")
#     print(wurdle_wurds)

    #     wurdle.append(string)
    # wurdle_wurds = random.choice(wurdle)
    # wurdle_wurds = random.replace("\n", "")
    # print(wurdle_wurds)


    # wurd_length = range(len(wurdle_wurds))
    # for num in wurd_length:
    #     underscores.append('_')
    # underscores = "".join(underscores)
    # print(" ".join(underscores))
    
    # wurd_display = ["_"] * len(wurdle_wurds)

#guesses


    # guess = input('Guess a letter: ').upper()
    # guessed_letters.append(guess)
    # if guess != wurdle_wurds:
    #     guess_count += 1
    # if guess == 'Quit':
    #     end_game = True
    # if guess_count >= 8:
    #     end_game =True

# while guess != 'Quit' and end_game == True:

#shows correct letters in hidden word

    # for index in range(len(wurdle_wurds)):
    #     if wurdle_wurds[index] == guess:
    #         underscores = underscores[0:index] + guess + underscores[index+1:]
    #         guess + underscores[index+1:]
    # print(underscores)



    # if guess in wurdle_wurds:
    #     print("Correct! Great guess.")
    #     guessed_letters.append(guess)
    #     guess = input('Guess again... ')

    # else: 
    #     guess != wurdle_wurds
    #     guess = input('Guess again... ')
    #     guess_count += 1
    #     # print("Number of guesses made: " + (str(guess_count)))
    #     # guessed_letters.append(user_input)
    #     player_letter = input(f"You have made {guess_count} of 8 guesses left. What letter do you guess?").upper()  # uppercase the users input
    #     guess_list.append(player_letter)
    #     guessed_letters += f" {player_letter}, "
    #     print(guessed_letters)   
    #     if guess_count >= 8:
#             end_game =True
#             print(str(wurdle_wurds))





# if guess == 'Quit':
#     end_game = True
#     # print(random_word)
#     input('You sure?(Y/N)')
#     # if input == ('Y'):
# #somehow reinitialize loop
        
# #need a function to end game if word is guessed.

# if guess_count >= 8:
#     end_game =True
#     print(str(wurdle_wurds))
#     input('Again?(Y/N)')
    
    
    

if __name__ == "__main__":
    play_game()