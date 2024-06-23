# Made by: Omer Abdelwahab

import curses
from curses import wrapper
from colorama import Fore, Style
import sys
import time
import random


def main():
    print(Fore.CYAN + "Welcome to the typing speed test!")
    print(Fore.RESET, end = "")
    time.sleep(1)

    while True:
        inp = input("Press Enter to play... ")
        if inp == "":
            wpm, accuracy, elapsed_time = wrapper(test)
            print(end_screen(wpm, accuracy, elapsed_time))
            break
        else:
            if input("Incorrect input. Would you like to exit the program? (Y/N) ").lower() == "y":
                sys.exit(Fore.RED + "Program was terminated." + Fore.RESET)

def calculate_accuracy(expected_inp, actual_inp):
    """
    Calculates the accuracy of the user during the test.

    expected_input: Required parameter, a list of the target keys to be typed in.
    actual_input: Required parameter, a list of the inputted keys by the user.
    """

    errors = 0
    for i,c in enumerate(actual_inp):
        if c == expected_inp[i]:
            pass

        else:
            errors += 1


    acc = round((len(expected_inp) - errors) / len(expected_inp) * 100, 1)
    return acc


def calculate_wpm(correct_chars, time_taken):
    """
    Calculates the typing speed of the user in words-per-minute.

    correct_chars: Required parameter, integer which represents the number of correct keys inputted by the user.
    time_taken: Required parameter, floating point value which represents the time taken for the user to complete the test.
    """

    return round((correct_chars/5)/(time_taken/60))


def end_screen(wpm = 0, typing_accuracy = 0, time_elapsed = 0):
    """
    Generates an end-screen which displays the user's test results, which includes their typing speed in words-per-minute,
    percentage accuracy and time taken to complete the test.

    wpm: Integer which represents the typing speed of the user in words-per-minute.
    typing_accuracy: Integer which represents the accuracy of the user's typing throughout the test.
    time_elapsed: Floating point value which represents the time taken for the user to complete the test.
    """

    return f"""\n\n\n{Fore.CYAN}{Style.BRIGHT}You have completed the test!{Style.RESET_ALL}
{Fore.GREEN}####################
{Fore.WHITE}WPM = {Fore.BLUE}{wpm}
{Fore.WHITE}Time Taken = {Fore.BLUE}{time_elapsed} seconds
{Fore.WHITE}Accuracy = {Fore.BLUE}{typing_accuracy}%
{Fore.GREEN}#################### {Fore.RESET}"""



def generate_words(n):
    """Generates n random words from 'words.txt'."""

    lst = []
    with open("words.txt", "r") as file:
        lines = file.readlines()
        for _ in range(n):
            lst.append(random.choice(lines).strip())

        words = ""
        for word in lst:
            words = words + word + " "
        return words.strip()


def num_of_words(s):
    """Prompts the user to choose the amount of words they wish to type."""

    while True:
        s.addstr(0, 0, "How many words would you like to type?")
        s.addstr(1, 0, "1) 10")
        s.addstr(2, 0, "2) 15")
        s.addstr(4, 0, "Choose a number 1-2: ")
        n = s.getkey()
        s.clear()
        s.refresh()
        if n == "1":
            return 10
        elif n == "2":
            return 15


def test(s):
    """Generates the typing speed test."""

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    test_text = generate_words(num_of_words(s))
    s.addstr(0, 0, test_text)

    user_inp = []
    correct_inp = []

    times_executed = 0

    while True:
        key = s.getkey()
        if times_executed == 0:
            start_timer = time.time()

        times_executed += 1

        s.addstr(0, 0, test_text)

        if key in ("KEY_BACKSPACE", "\x7f", "\b"):    #Backspace key
            if len(user_inp) > 0:
                del user_inp[-1]                    #delete last item in the list
        else:
            user_inp.append(key)
            index_of_key = user_inp.index(key)
            if key == test_text[index_of_key]:
                correct_inp.append(key)

        if key == "\n":
            sys.exit(Fore.RED + "Program was terminated." + Fore.RESET)

#Assign correct color to each inputted key and overlay it on top of expected key
        for i,c in enumerate(user_inp):
            correct_char = test_text[i]
            if c == correct_char:
                color = curses.color_pair(1)
            else:
                color = curses.color_pair(2)

            s.addstr(0, i, c, color)

        s.refresh()


        if len(user_inp) == len(test_text):
            end_timer = time.time()
            elapsed_time = round(end_timer - start_timer, 2)
            break

    w = calculate_wpm(len(correct_inp), elapsed_time)
    a = calculate_accuracy(test_text, user_inp)
    return w, a, elapsed_time


if __name__ == "__main__":
    main()
