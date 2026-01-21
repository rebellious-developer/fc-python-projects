#!/usr/bin/env python3
"""
A simple game of Rock-Paper-Scissors in Python that takes the input as Rock, Paper, or Scissors and allows you to compete against the computer.

Requirements:
- Instructions provide the choices with corresponding numbers. 1=Rock, 2=Paper, 3=Scissors.
- The user should be prompted to enter the number corresponding to their choice.
- After the user inputs their choice, the computer randomly selects its choice.
- Input validation:
  * The input must be a valid integer number.
  * The number must be within the range of 1 to 3.
- Input error handling:
  * If the input is not a valid integer, display an error message: "Invalid input: Please enter a valid number between 1 and 3."
  * If the input is outside the specified range, display an error message: "Input out of range: Please enter a number between 1 and 3."
- Win/loss conditions:
  * Rock (1) beats Scissors (3).
  * Scissors (3) beats Paper (2).
  * Paper (2) beats Rock (1).
  * The same choices result in a tie.
- The game should repeat until the user decides to quit via CTRL+C.
- Output:
  * Appropriate messages based on the user's choices and the computer's choices.
  * If the user's choice beats the computer's choice, display "WIN!" on a newline.
  * If the computer's choice beats the user's choice, display "LOSE!" on a newline.
  * If it's a tie, display "TIE!" on a newline.
"""

import random


def main():
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    print("Welcome to Rock-Paper-Scissors!\n")
    print("Enter the number corresponding to your choice:")
    print("1 = Rock (beats Scissors)")
    print("2 = Paper (beats Rock)")
    print("3 = Scissors (beats Paper)")
    print("\nPress CTRL+C to quit the game.")

    while True:
        try:
            user_input = input("Your choice (1-3): ")
            user_choice = int(user_input)

            if user_choice < 1 or user_choice > 3:
                print("Input out of range: Please enter a number between 1 and 3.")
                continue

            computer_choice = random.randint(1, 3)
            print(f"Computer chose: {choices[computer_choice]}")

            if user_choice == computer_choice:
                print("TIE!\n")
            elif (
                (user_choice == 1 and computer_choice == 3)
                or (user_choice == 2 and computer_choice == 1)
                or (user_choice == 3 and computer_choice == 2)
            ):
                print("WIN!\n")
            else:
                print("LOSE!\n")

        except ValueError:
            print("Invalid input: Please enter a valid number between 1 and 3.")
        except KeyboardInterrupt:
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
