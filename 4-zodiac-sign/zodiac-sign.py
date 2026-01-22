#!/usr/bin/env python3
"""
A simple zodiac sign calculator in Python.

Requirements:
- Use pandas to handle CSV file operations.
- The user will be prompted to enter their NAME then their BIRTHDATE (in the format DD-MM).
- Input validation
  * The NAME must be at least 2 characters long after trimming leading and trailing whitespace.
  * The BIRTHDATE must be in the format DD-MM and represent a valid date (note that year is not important for determining the Zodiac sign).
- Input error handling:
  * If name is invalid, display an error message: "Invalid input: Name must be at least 2 characters long."
  * If birthdate is invalid, display an error message: "Invalid input: Birthdate must be in the format DD-MM and represent a valid date."
- The program will extract the month and day from the birthdate.
- Use pandas to load the zodiac sign date ranges from a predefined CSV file named zodiac_signs.csv. This will be loaded into a DataFrame.
- Based on the extracted month and day, the program will determine the corresponding Zodiac sign by comparing the date against the date ranges in the DataFrame.
- If a matching Zodiac sign is found, the program will output: "Hello {NAME}, your Zodiac sign is {ZODIAC_SIGN}."
- If no matching sign is found, display an error message: "Could not determine Zodiac sign for the given birthdate."
- The program will store the user's NAME, BIRTHDATE, and determined ZODIAC_SIGN in a CSV file named user_zodiac_signs.csv using pandas. If the file already exists, it will append the new entry; otherwise, it will create a new file with appropriate headers.
- If a record already exists for the same NAME and BIRTHDATE, it will not create a duplicate entry and will instead display: "Record for {NAME} with birthdate {BIRTHDATE} already exists."
- Once the data is stored, display: "Your Zodiac sign information has been saved successfully."
- The program will repeat this workflow until the user decides to quit via CTRL+C.
- When capturing any particular input then failure will only result in re-prompting for that specific input, not restarting the entire workflow.
"""

import os
import re
from datetime import datetime

import pandas as pd


def load_zodiac_signs_dataset():
    """Loads the zodiac signs and their date ranges from a CSV file into a Pandas DataFrame."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_name = "zodiac_signs.csv"
    csv_path = os.path.join(script_dir, csv_name)

    try:
        zodiac_signs_df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("Zodiac signs data file not found.")
        raise

    if zodiac_signs_df.empty:
        print("Zodiac signs data file is empty.")
        raise ValueError("Empty zodiac signs data.")

    return zodiac_signs_df


def write_user_zodiac_sign_dataset(name, birthdate, zodiac_sign):
    """Writes the user's zodiac sign information to a CSV file via Pandas."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_name = "user_zodiac_signs.csv"
    csv_path = os.path.join(script_dir, csv_name)

    birthdate_dd_mm = birthdate.strftime("%d-%m")

    user_data = {
        "Name": [name],
        "Birth_Date": [birthdate_dd_mm],
        "Zodiac_Sign": [zodiac_sign],
    }
    user_df = pd.DataFrame(user_data)

    try:
        existing_df = pd.read_csv(csv_path)

        # Check for duplicates
        duplicate = existing_df[
            (existing_df["Name"] == name)
            & (existing_df["Birth_Date"] == birthdate_dd_mm)
        ]

        if not duplicate.empty:
            print(f"Record for {name} with birthdate {birthdate_dd_mm} already exists.")
            return

        updated_df = pd.concat([existing_df, user_df], ignore_index=True)
        updated_df.to_csv(csv_path, index=False)
    except FileNotFoundError:
        user_df.to_csv(csv_path, index=False)

    print(f"Your Zodiac sign information has been saved successfully to '{csv_name}'.")


def capture_name():
    """Captures and validates the user's name input."""
    name = input("Enter your NAME: ").strip()
    if len(name) < 2:
        print("Invalid input: Name must be at least 2 characters long.")
        return None
    return name


def repeat_capture_name():
    """Repeats capturing name until valid input is received or user quits."""
    name = None
    while name is None:
        try:
            name = capture_name()
        except KeyboardInterrupt:
            raise
    return name


def capture_birthdate():
    """Captures and validates the user's birthdate input."""
    birthdate_input = input("Enter your BIRTHDATE (DD-MM): ").strip()
    try:
        # Make sure the format is DD-MM using a regular expression
        if not re.match(r"^\d{2}-\d{2}$", birthdate_input):
            raise ValueError

        # Make sure it's a valid date by attempting to parse it
        birthdate = datetime.strptime(
            f"{birthdate_input}-1980",
            "%d-%m-%Y",  # Note: Year is a placeholder
        )
        return birthdate
    except ValueError:
        print(
            "Invalid input: Birthdate must be in the format DD-MM and represent a valid date."
        )
        return None


def repeat_capture_birthdate():
    """Repeats capturing birthdate until valid input is received or user quits."""
    birthdate = None
    while birthdate is None:
        try:
            birthdate = capture_birthdate()
        except KeyboardInterrupt:
            raise
    return birthdate


def find_zodiac_sign(birthdate: datetime, zodiac_signs_df: pd.DataFrame):
    """Finds the zodiac sign for the given birthdate using the zodiac signs DataFrame."""
    for _, row in zodiac_signs_df.iterrows():
        start_month = row["Start_Month"]
        start_day = row["Start_Day"]
        end_month = row["End_Month"]
        end_day = row["End_Day"]
        birth_month = birthdate.month
        birth_day = birthdate.day

        # Handle date ranges that span the end of the year
        if start_month > end_month:  # Wraps around year end (e.g., Capricorn)
            if birth_month >= start_month or birth_month <= end_month:
                if (
                    (birth_month == start_month and birth_day >= start_day)
                    or (birth_month == end_month and birth_day <= end_day)
                    or (birth_month > start_month or birth_month < end_month)
                ):
                    return row["Sign"]
        else:  # Normal range within same year
            if start_month <= birth_month <= end_month:
                if (
                    (birth_month == start_month and birth_day >= start_day)
                    or (birth_month == end_month and birth_day <= end_day)
                    or (start_month < birth_month < end_month)
                ):
                    return row["Sign"]
    return None


def zodiac_sign_capture(zodiac_signs_df: pd.DataFrame):
    """Captures user input for name and birthdate, determines zodiac sign, and stores the information."""
    print("-----------------------------")
    name = repeat_capture_name()
    birthdate = repeat_capture_birthdate()
    zodiac_sign = find_zodiac_sign(birthdate, zodiac_signs_df)

    if zodiac_sign:
        print(f"\nHello {name}, your Zodiac sign is {zodiac_sign}.")
        write_user_zodiac_sign_dataset(name, birthdate, zodiac_sign)
    else:
        print("\nCould not determine Zodiac sign for the given birthdate.")


def main():
    print("Welcome to Zodiac Sign Calculator!\n")
    print("\nPress CTRL+C at any point to quit.")

    try:
        zodiac_signs_df = load_zodiac_signs_dataset()
    except Exception as e:
        print(f"Failed to load zodiac signs data: {e}")
        return

    print("\nZodiac Sign Data Loaded Successfully")
    print("Zodiac Signs Dataset:")
    print(zodiac_signs_df)

    while True:
        try:
            zodiac_sign_capture(zodiac_signs_df)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return


if __name__ == "__main__":
    main()
