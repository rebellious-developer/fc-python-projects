#!/usr/bin/env python3
"""
A binary search algorithm test implementation in Python.

Requirements:
- Use numpy where possible for this exercise (since we are dealing with just numbers)
- Generate a random list of X integers to be searched (in a random order).
- Run a quick sort on it so the numbers are in ascending order.
- The user should be prompted to enter an integer to search for in the list.
- Input validation
  * The value must be an integer.
- Input error handling:
  * If the target is not an integer, re-prompt the user until a valid integer is entered.
- Perform a binary search to find the integer in the sorted list.
- Repeat until the user decides to quit via CTRL+C.
- Output:
  * "Welcome to Binary Search Example!" on a newline.
  * "A random list of 20 integers from 1 to 1000 has been generated and sorted." on a newline.
  * The sorted list of integers in CSV format on a newline
  * "Press CTRL+C to quit." on a newline.
  * "Enter the number to search for (1 - 1000):" on a newline.
  * The input prompt ">>
  * If the input is not a valid integer, display an error message: "Invalid input: Please enter a valid number between 1 and 1000.
  * If the input is outside the specified range, display an error message: "Input out of range: Please enter a number between 1 and 1000."
  * If the choice is found in the list via the binary search, display "SUCCESS! Integer {user_choice} was FOUND at index {index}."
  * If the choice is not found in the list via the binary search, display "FAILURE! Integer {user_choice} was NOT FOUND in the list."
"""

import numpy as np


def binary_search(arr, target):
    """Performs binary search on a sorted array."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main():
    # Generate a random list of integers and sort it in ascending order
    int_count = 20
    min_value = 1
    max_value = 1000
    int_list = np.random.randint(min_value, max_value + 1, size=int_count)
    sorted_int_list = np.sort(int_list)

    print("Welcome to Binary Search Example!\n")
    print(
        f"A random list of {int_count} integers from {min_value} to {max_value} has been generated and sorted."
    )
    print("Sorted List: " + ", ".join(map(str, sorted_int_list)))
    print("\nPress CTRL+C to quit.")

    while True:
        try:
            print(f"Enter the number to search for ({min_value} - {max_value}):")
            user_input = input(">> ")
            user_choice = int(user_input)

            if user_choice < min_value or user_choice > max_value:
                print(
                    f"Input out of range: Please enter a number between {min_value} and {max_value}."
                )
                continue

            # Perform binary search
            result = binary_search(sorted_int_list, user_choice)

            if result != -1:
                print(f"SUCCESS! Integer {user_choice} was FOUND at index {result}.")
            else:
                print(f"FAILURE! Integer {user_choice} was NOT FOUND in the list.")

        except ValueError:
            print(
                f"Invalid input: Please enter a valid number between {min_value} and {max_value}."
            )
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue


if __name__ == "__main__":
    main()
