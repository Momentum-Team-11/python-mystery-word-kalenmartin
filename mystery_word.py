import random
import re

def main():
    answer = wurdle_level()
    return loop_de_loop(answer)

file = open("words.txt")
dict = file.read()
dict = dict.lower().split()


def easy_wurds(wurd_list):
    easy_list = []
    for wurd in wurd_list:
        if len(wurd) >= 4 and len(wurd) <= 6:
            easy_list.append(wurd)
    return easy_list


def medium_wurds(wurd_list):
    medium_list = []
    for wurd in wurd_list:
        if len(wurd) >= 6 and len(wurd) <= 8:
            medium_list.append(wurd)
    return medium_list


def hard_wurds(wurd_list):
    hard_list = []
    for wurd in wurd_list:
        if len(wurd) >= 8:
            hard_list.append(wurd)
    return hard_list


def random_wurd(wurd_list):
    correct_wurd = random.choice(wurd_list)
    return correct_wurd


def display_wurd(wurd, guesses):
    progress_display = []
    for letter in wurd:
        if letter in guesses:
            progress_display.append(letter)
        else:
            progress_display.append('_')
    progress_display = ' '.join(progress_display)
    progress_display = progress_display.upper()
    return progress_display


def is_wurd_complete(wurd, guesses):
    progress = display_wurd(wurd, guesses)
    if '_' in progress:
        return False
    else:
        return True


def wurdle_level():
    print("\n**************************************\n*************** Wurdle ***************\n**************************************\n")
    print("You have 8 attempts to pretend that this is the real Wordle.\n\n\n")
    level = input("Do you want to feel good about yourself or not? Choose easy, medium, or hard.\n")
    level = level.lower()
    if level == 'easy':
        answer = random_wurd(easy_wurds(dict))
    elif level == 'medium':
        answer = random_wurd(medium_wurds(dict))
    else:
        answer = random_wurd(hard_wurds(dict))
    return answer


def loop_de_loop(answer):
    guesses = []
    fails = 0
    print("\nYou're looking for a wurd with {} letters.\n".format(len(answer)))
    while is_wurd_complete(answer, guesses) == False:
        current_guess = (input("Cool, take a guess.\n\n")).lower()
        if len(current_guess) > 1:
            print("One letter only. plz and thx.")
        elif current_guess not in guesses:
            if current_guess not in answer:
                print("That letter isn't in your wurd.\n")
                fails += 1
            else:
                print("Nice! That letter is in your wurd.\n")
        else:
            print("Come on, you already guessed that letter.\n")
        guesses.append(current_guess)
        print(display_wurd(answer, guesses))
        print("These are your guesses so far: {}\n".format(guesses))
        print("-> You have {} guesses left<-\n".format(8 - fails))
        if fails >= 8:
            break
    if fails >= 8:
        wurdle_lose = input(("You lose! The wurd was {}.\nDo you want to play again? enter yes or no.\n\n".format(answer)))
        wurdle_lose.lower()
        if wurdle_lose == 'yes':
            return main()
        else:
            print("Raddddd")
    else:
        wurdle_win = input(("You won the Wurdle! Play again? enter yes or no.\n"))
        wurdle_win.lower()
        if wurdle_win == 'yes':
            return main()
        else:
            print("Okay fine")


if __name__ == '__main__':
    main()