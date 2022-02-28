import random
import re

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


def get_level():
    print("\n***Wurdle***\n")
    print("You have 8 attempts to pretend that this is the real Wordle.\n")
    level = input("What difficulty setting do you want? Please enter easy, medium or hard.\n")
    level = level.lower()
    if level == 'easy':
        answer = random_wurd(easy_wurds(dict))
    elif level == 'medium':
        answer = random_wurd(medium_wurds(dict))
    else:
        answer = random_wurd(hard_wurds(dict))
    return answer


def gameplay_loop(answer):
    guesses = []
    fails = 0
    print("You're looking for a wurd with {} letters.".format(len(answer)))
    while is_wurd_complete(answer, guesses) == False:
        current_guess = (input("Okay, take a guess!\n")).lower()
        if len(current_guess) > 1:
            print("One letter only. plz and thx.")
        elif current_guess not in guesses:
            if current_guess not in answer:
                print("That letter isn't in your wurd.")
                fails += 1
            else:
                print("Nice! That letter is in your wurd.")
        else:
            print("You already guessed that letter.")
        guesses.append(current_guess)
        print(display_wurd(answer, guesses))
        print("These are your guesses so far: {}".format(guesses))
        print("You have {} guesses left.\n".format(8 - fails))
        if fails >= 8:
            break
    if fails >= 8:
        play_again_lose = input(("You lose! The wurd was {}. If you want to play again, enter yes or no.\n".format(answer)))
        play_again_lose.lower()
        if play_again_lose == 'yes':
            return main()
        else:
            print("Okay fine")
    else:
        play_again_win = input(("You won! Do you want to play again? enter yes or no.\n"))
        play_again_win.lower()
        if play_again_win == 'yes':
            return main()
        else:
            print("Rad")


def main():
    answer = get_level()
    return gameplay_loop(answer)

if __name__ == '__main__':
    main()