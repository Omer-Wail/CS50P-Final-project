# CS50P-Final-project
# Typing Speed Test
#### Video Demo: https://youtu.be/u1NqGZAdTP4
## Description:
Generates an interactive typing speed test which displays the user's typing speed(wpm), accuracy(percentage) and time taken to complete the test(seconds) upon finishing.
## Usage
`python project.py`

![Image](https://github.com/Omer-Wail/CS50P-Final-project/blob/main/Images/img1.png)

After inputting the ENTER key, the user will be transported to the `curses` terminal.

![Image](https://github.com/Omer-Wail/CS50P-Final-project/blob/main/Images/img2.png)

Input 1 or 2 to start the test. For the sake of this example, 1 is inputted.

![Image](https://github.com/Omer-Wail/CS50P-Final-project/blob/main/Images/img3.png)

The user can then begin the typing test. It is important to note that the time will only start once the first key is inputted, so the user can start whenever they are ready.

A correct character will be colored green

![Image](https://github.com/Omer-Wail/CS50P-Final-project/blob/main/Images/img4.png)

and an incorrect character will be colored red.

![Image](https://github.com/Omer-Wail/CS50P-Final-project/blob/main/Images/img5.png)

The user can exit the program at any point during the test by pressing the ENTER key, which will cause the program to exit via `sys.exit()` and show this message:

![Image](https://github.com/Omer-Wail/CS50P-Final-project/blob/main/Images/img6.png)

Upon inputting the last key, the user will be transported back to the original terminal with the tests results displayed:

![Image](https://github.com/Omer-Wail/CS50P-Final-project/blob/main/Images/img7.png)


## Files
### project.py
This is the main program which creates the typing speed test, using the help of `words.txt` to generate random words for the test.

### Functions:
#### main()
Generates a start screen which welcomes the user and prompts them to play by pressing the ENTER key, and, based on the user's input, starts the test.

#### calculate_accuracy(expected_inp, actual_inp)
Calculates the accuracy of the user during the test.

*expected_input*: Required parameter, a list of the target keys to be typed in.

*actual_input*: Required parameter, a list of the inputted keys by the user.

#### calculate_wpm(correct_chars, time_taken)
Calculates the typing speed of the user in words-per-minute.

*correct_chars*: Required parameter, integer which represents the number of correct keys inputted by the user.

*time_taken*: Required parameter, floating point value which represents the time taken for the user to complete the test.

#### end_screen(wpm = 0, typing_accuracy = 0, time_elapsed = 0)
Generates an end-screen which displays the user's test results, which includes their typing speed in words-per-minute,
    percentage accuracy and time taken to complete the test.

*wpm*: Integer which represents the typing speed of the user in words-per-minute.

*typing_accuracy*: Integer which represents the accuracy of the user's typing throughout the test.

*time_elapsed*: Floating point value which represents the time taken for the user to complete the test.

#### generate_words(n)
Generates n random words from `words.txt`.

#### num_of_words(s)
Prompts the user to choose from two options which represent the amount of words to be generated for the test.

#### test(s)
Generates the typing speed test by utilizing the [curses](https://docs.python.org/3/library/curses.html#module-curses) module. It first generates the amount of words for the test by calling the `generate_words` function based on the return value of the `num_of_words` and displays them on the screen, which signals the start of the test. Each correct key inputted by the user will be displayed in green color, while each incorrect key inputted by the user will be displayed in red color. The [time](https://docs.python.org/3/library/time.html) module is used to calculate the time taken to complete the test. The `calculate_accuracy` and the `calculate_wpm` functions are used to calculate the accuracy and typing speed of the user respectively. Returns typing speed(wpm), accuracy and time taken.

### words.txt
Contains 100 of the most commonly used english words, one per line.

## Author: Omer Abdelwahab
