# Python Projects (Future Connect)

## Summary
This is a project created to hold the `Python Projects` module code that I created as part of the Data Science training/certification course with Future Connect. The repo will contain basic Python scripts demonstrating the fundamental programming concepts and techniques necessary for the assigned exercises.

## How I created this project
1. Created this project folder (fc-python-projects)

2. Ran the following shell commands from inside the project folder:
```bash
git init
touch README.md
subl ./README.md
(then edited the contents via Sublime Text and saved)
git add README.md
git commit -m "Initial commit of this repo with a basic README.md file"
```

3. Then I used GH CLI to create the repo on my GH account using the local GIT repo:
```bash
gh repo create
? What would you like to do? Push an existing local repository to GitHub
? Path to local repository .
? Repository name fc-python-projects
? Description This is a project created to hold the `Python Projects` module code that I created as part of the Data Science training/certification course with Future Connect. The repo will contain basic Python scripts demonstrating the fundamental programming concepts and techniques necessary for the assigned exercises.
? Visibility Public
✓ Created repository rebellious-developer/fc-python-projects on GitHub
  https://github.com/rebellious-developer/fc-python-projects
? Add a remote? Yes
? What should the new remote be called? origin
✓ Added remote git@github.com:rebellious-developer/fc-python-projects.git
? Would you like to push commits from the current branch to "origin"? Yes
To github.com:rebellious-developer/fc-python-projects.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

5. Then I opened up the folder in Visual Studio Code for all further editing.

6. Setup a basic `copilot-instructions.md` file for this project (because I like to use Co-Pilot on all projects for code assistance)

7. Added a bare minimum basic Python project structure for such a simple app:
.editorconfig
.gitignore
.python-version
requirements.txt

8. Committed and pushed all my changes:
```bash
git add .
git commit -m "Updated README plus foundation files"
git push origin
```


9. I then went through the projects and added a folder for each and a single python file for each. File format is `{projectnum}-{projectname}.py`

These are:
- [1-rock-paper-scissors](1-rock-paper-scissors.py) — A simple game of Rock-Paper-Scissors in Python that takes the input as Rock, Paper, or Scissors and allows you to compete against the computer.

## Projects
The projects were:

### Project 1: Rock Paper Scissors Game

#### You want to create a simple game of Rock-Paper-Scissors in Python that takes the input as Rock, Paper, or Scissors and allows you to compete against the computer.
```Python
# See folder `1-rock-paper-scissors` for my code

"""
Sample output:-

Welcome to Rock-Paper-Scissors!

Enter the number corresponding to your choice:
1 = Rock (beats Scissors)
2 = Paper (beats Rock)
3 = Scissors (beats Paper)

Press CTRL+C to quit the game.
Your choice (1-3): Hello
Invalid input: Please enter a valid number between 1 and 3.
Your choice (1-3): -2
Input out of range: Please enter a number between 1 and 3.
Your choice (1-3): 5
Input out of range: Please enter a number between 1 and 3.
Your choice (1-3): 1
Computer chose: Scissors
WIN!

Your choice (1-3): 2
Computer chose: Paper
TIE!

Your choice (1-3): 3
Computer chose: Rock
LOSE!

Your choice (1-3): ^C
Thanks for playing! Goodbye!
"""
```

#### Notes:
- I entered the requirements in the docblock at the top of the Python script
- I used an infinite while loop with a KeyboardInput exception handler to keep the game running until the user pressed CTRL+C
- Each iteration of the game the computer would pick a different choice but not reveal it until the player enteres their choice

-----------------

### Project 2: Binary Search Algorithm

#### You want to implement a Binary Search algorithm in Python to efficiently search for a target value in a sorted list.
```Python
# See folder `2-binary-search-algorithm` for my code

"""
Sample output:-

Welcome to Binary Search Example!

A random list of 20 integers from 1 to 1000 has been generated and sorted.
Sorted List: 41, 133, 182, 244, 331, 331, 377, 390, 419, 453, 506, 525, 573, 578, 656, 687, 729, 786, 850, 912

Press CTRL+C to quit.
Enter the number to search for (1 - 1000):
>> 12
FAILURE! Integer 12 was NOT FOUND in the list.
Enter the number to search for (1 - 1000):
>> -1
Input out of range: Please enter a number between 1 and 1000.
Enter the number to search for (1 - 1000):
>> 10000
Input out of range: Please enter a number between 1 and 1000.
Enter the number to search for (1 - 1000):
>> 41
SUCCESS! Integer 41 was FOUND at index 0.
Enter the number to search for (1 - 1000):
>> 656
SUCCESS! Integer 656 was FOUND at index 14.
Enter the number to search for (1 - 1000):
>> ^C
Goodbye!
"""
```

#### Notes:
- I entered the requirements in the docblock at the top of the Python script
- I used an infinite while loop with a KeyboardInput exception handler to keep the input loop running until the user pressed CTRL+C
- The array is randomly generated ONCE using 20 numbers from 1 - 1000
- The array is then sorted via numpy quicksort
- A basic binary search is performed after each valid user input

-----------------

### Project 3: Email to one or multiple recipients

#### You want to write a Python program that can send emails to one or multiple recipients using an email account.
```Python
# See folder `3-email-multiple-recipients` for my code

"""
Sample output:-

Configuration loaded:{'smtp_server': 'localhost', 'smtp_port': 1025, 'smtp_username': '', 'smtp_password': '', 'from_address': 'your_mom@example.com', 'to_addresses': ['scott@example.com'], 'cc_addresses': [], 'bcc_addresses': [], 'subject': 'Test Email from Your Mom', 'body': 'This is a test email from your mom.', 'use_tls': False}

Email sent successfully to ['scott@example.com'] with CC to [] and BCC to [].

From the terminal running the SMTP server:
python3 -m aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:1025
---------- MESSAGE FOLLOWS ----------
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Test Email from Your Mom
From: Sender Name <your_mom@example.com>
To: scott@example.com
Cc: 
X-Peer: ('127.0.0.1', 53698)

This is a test email from your mom.
------------ END MESSAGE ------------

"""
```

#### Notes:
- I entered the requirements in the docblock at the top of the Python script
- For this I decided to use a simple SMTP debugging lib named `aiosmtpd` and start it in my terminal via:
python3 -m aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:1025
- I decided to hardcode the default email params but allow overriding from a config.json file

-----------------

### Project 4: Zodiac Sign

#### Given the birthdate and name of the person, you want to create a Python program to determine the corresponding Zodiac sign based on the date. Write a Python program that takes name and birthdate as input and outputs the corresponding Zodiac sign and store it in a file using Pandas.
```Python
# See folder `4-zodiac-sign` for my code

"""
Sample output:-

Welcome to Zodiac Sign Calculator!


Press CTRL+C at any point to quit.

Zodiac Sign Data Loaded Successfully
Zodiac Signs Dataset:
           Sign  Start_Month  Start_Day  End_Month  End_Day
0     Capricorn           12         22          1       19
1      Aquarius            1         20          2       18
2        Pisces            2         19          3       20
3         Aries            3         21          4       19
4        Taurus            4         20          5       20
5        Gemini            5         21          6       20
6        Cancer            6         21          7       22
7           Leo            7         23          8       22
8         Virgo            8         23          9       22
9         Libra            9         23         10       22
10      Scorpio           10         23         11       21
11  Sagittarius           11         22         12       21
-----------------------------
Enter your NAME: Scott
Enter your BIRTHDATE (DD-MM): 27-07

Hello Scott, your Zodiac sign is Leo.
Your Zodiac sign information has been saved successfully to 'user_zodiac_signs.csv'.
-----------------------------
Enter your NAME: Bill
Enter your BIRTHDATE (DD-MM): 01-01

Hello Bill, your Zodiac sign is Capricorn.
Your Zodiac sign information has been saved successfully to 'user_zodiac_signs.csv'.
-----------------------------
Enter your NAME: n
Invalid input: Name must be at least 2 characters long.
Enter your NAME:   
Invalid input: Name must be at least 2 characters long.
Enter your NAME: John
Enter your BIRTHDATE (DD-MM): -12/15
Invalid input: Birthdate must be in the format DD-MM and represent a valid date.
Enter your BIRTHDATE (DD-MM): 30-02
Invalid input: Birthdate must be in the format DD-MM and represent a valid date.
Enter your BIRTHDATE (DD-MM): Hello
Invalid input: Birthdate must be in the format DD-MM and represent a valid date.
^C
Goodbye!
"""
```

#### Notes:
- TODO

-----------------

### Project 5: Large File Renamer

#### Often, we have a large number of files in a directory with names that do not follow a specific pattern or are not easy to understand. Renaming each file manually can be time-consuming and error-prone. To solve this problem, we need a program that can rename a large number of files in bulk, based on a specified pattern. Develop a Python program that takes a directory path and a pattern as input, and renames all the files in the directory that match the pattern to a new name that follows the specified pattern?


```Python
# See folder `5-large-file-renamer` for my code

"""
Sample output:-

TODO
"""
```

#### Notes:
- TODO

-----------------

### Project 6: Web Scraping

#### The task is to scrape the list of largest companies in US by revenue form wikipedia using Beautiful Soup in Python. The data required to be extracted includes the rank, name of company, Industry, Revenue, Revenue growth, Headquarters for the top 20 US companies by revenue.
```Python
# See folder `4-zodiac-sign` for my code

"""
Sample output:-

TODO
"""
```

#### Notes:
- TODO

-----------------

### My Notes:
- Overall the activities were very simple and I kept the solutions very simple since the goal of this module is to prove I can write basic Python code to an instructor
- Activity 6 was pretty vague and not well defined so I chose the simplest (laziest?) solution. I could have chosen expression parsing but it was more work than I felt like doing for such a basic module.

`[END OF DOCUMENT]`
