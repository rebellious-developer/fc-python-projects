# Python Activities (Future Connect)

## Summary
A project that I created to host various assignment activities from the foundation Python module for my Data Science certification course with Future Connect.

Contains the answers to the following

## How I created this project
1. Created this project folder (fc-python-activities)

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
? Repository name fc-python-activities
? Description A project that I created to host various assignment activities from the foundation Python module for my Data Science certification course with Future Connect.
? Visibility Public
✓ Created repository rebellious-developer/fc-python-activities on GitHub
  https://github.com/rebellious-developer/fc-python-activities
? Add a remote? Yes
? What should the new remote be called? origin
✓ Added remote git@github.com:rebellious-developer/fc-python-activities.git
? Would you like to push commits from the current branch to "origin"? Yes
To github.com:rebellious-developer/fc-python-activities.git
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

9. I then all the activities and added a .py file for each activity. File format is `{activitynum}-{name}.py`

These are:
- [1-fizzbuzz.py](1-fizzbuzz.py) — Simple FizzBuzz implementation that prints 1..100 with Fizz/Buzz/FizzBuzz rules. Main entry: [`fizzbuzz`](1-fizzbuzz.py).
- [2-swap-string-case.py](2-swap-string-case.py) — Reads a string from the console and swaps letter case. Key function: [`str_swap_case`](2-swap-string-case.py).
- [3-swap-two-numbers.py](3-swap-two-numbers.py) — Demonstrates swapping two numbers using a third variable and without using a third variable. Key functions: [`swap_with_third_variable`](3-swap-two-numbers.py), [`swap_without_third_variable`](3-swap-two-numbers.py).
- [4-fibanacci-till-number.py](4-fibanacci-till-number.py) — Generates the Fibonacci series up to a user-entered limit (0..1,000,000). Key function: [`generate_fibonacci_series`](4-fibanacci-till-number.py).
- [5-number-guess-game.py](5-number-guess-game.py) — Console number guessing game (1..1000) with input validation and attempt limiting. Main entry: [`main`](5-number-guess-game.py).
- [6-basic-two-number-calculator.py](6-basic-two-number-calculator.py) — Minimal two-number calculator handling +, -, *, / with validation and division-by-zero handling. Key function: [`calculate`](6-basic-two-number-calculator.py) and entry: [`main`](6-basic-two-number-calculator.py).


## Assignment Activities (with questions and answers)
The assigment activities and questions were:

### Activity 1: Fizz Buzz

#### 1: Write code in Python in which you can get “Fizz Buzz” for all numbers which can be divided by (3, 5, 15). The range should from (1 to 100).
```Python
# See file `1-fizzbuzz.py` for my code

"""
Sample output (first 16 numbers):-

1 : --
2 : --
3 : Fizz
4 : --
5 : Buzz
6 : Fizz
7 : --
8 : --
9 : Fizz
10 : Buzz
11 : --
12 : Fizz
13 : --
14 : --
15 : FizzBuzz
16 : --
"""
```

#### Questions:
**1. Which operator will you use in order to execute this code?**  
The modulo (aka "remainder") operator % (eg. 1.345 % 1 === .345). If something is divisible by a given number the remainder will be zero.

-----------------

### Activity 2: Swap Cases

#### 1: How to swap all uppercase characters to lowercase and vice versa?
```Python
# See file `2-swap-string-case.py` for my code

"""
Sample output:-

Enter a string: Tabul@R
Swapped case string: tABUL@r
"""
```

#### Questions:
**1. How the user will enter the character string?**  
I chose to use the `input()` function in Python which accepts user input from the CLI until the user presses ENTER. I could just have easily declared a hard-coded list or tuple and then looped through each item in the list and called str_swap_case for each.

**2. How will it swap?**  
It tests each character in sequence from 1 to EOL to see if it is a lower or upper character. Lower is converted into upper and pper is converted into lower.

**3. Which commands will be used to convert each other?**  
I used `char.lower()` to convert to lowercase and `char.upper()` to convert to uppercase.

-----------------

### Activity 3: Swap Numbers

#### 1: Swap any two numbers with and without using a 3rd variable.
```Python
# See file `3-swap-two-numbers.py` for my code

"""
Sample output:-

A=45, B=78
SwapWith3rdVar-Result: A=78, B=45
SwapWithNoVar-Result: A=78, B=45

A=100, B=200
SwapWith3rdVar-Result: A=200, B=100
SwapWithNoVar-Result: A=200, B=100

A=5, B=10
SwapWith3rdVar-Result: A=10, B=5
SwapWithNoVar-Result: A=10, B=5
"""
```

#### Questions:
**1. How you will create and store the value in 3rd variable?**  
Simply assign the first number variable to a temporary variable (eg. `temp = a`)

**2. How you will do it without the 3rd Variable?**  
The easiest way is tuple unpacking (eg. `a, b = b, a`)

-----------------

### Activity 4: Fibonacci Series

#### 1: Write code in Python which will give you the Fibonacci series up to any number when you enter it.
```Python
# See file `4-fibanacci-till-numbers.py` for my code

"""
Sample output:-
Enter a number (0 to 1,000,000): fish
ERROR: Invalid input: Please enter a valid integer number.

Enter a number (0 to 1,000,000): -45
ERROR: Input out of range: Please enter a number between 0 and 1,000,000.

Enter a number (0 to 1,000,000): 89344
Fibonacci series up to 89344 : 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025

Enter a number (0 to 1,000,000): 0
Fibonacci series up to 0 : 0

Enter a number (0 to 1,000,000): 1
Fibonacci series up to 1 : 0, 1
"""
```

#### Questions:
**1. How you will you handle when a user inputs ‘0’?**  
I'll just print '0', zero includes itself

**2. How will you handle when a user inputs ‘1’?**  
I'll print '0, 1', which is correct

**3. Which loops and statements do you use for the iterations?**  
A simple while loop will suffice comparing the current accumulated value (A) against the max limit the user entered (`while a <= limit`). Once the sequence is generated a simple print with a .join on the mapped sequence.

-----------------

### Activity 5: Number Guessing Game

#### 1: Create a game in which user guesses a random number in Python.
```Python
# See file `5-number-guess-game.py` for my code

"""
Sample output:-

Enter the first number: 3.54
Enter the second number: 93.2
Enter an operator (+, -, *, /): +
The result of 3.54 + 93.2 is: 96.74000000000001
"""
```

#### Questions:
**1. How will generate random number and how will you set the range?**  
I will use the built-in `random` module. The range is defined via `random.randint(min_num, max_num)` when `min_num = 1` and `max_num = 1000`

**2. How to add attempts in your code, that user can have only 5 attempts to play?**  
Define two variables `attempts` and `max_attempts`. Use `while attempts < max_attempts`. Increment attempts by 1 every time they enter a valid number.

**3. How will you subtract a attempt when user plays it one time?**  
There's no need to subtract an attempt. The user will play the game until it ends (or they exit via CTRL+C) then the program will exit.

**4. How will you show the ‘YOU WON!’ and ‘YOU LOST’ message?**  
WON: `print("YOU WIN!")`
LOST: `print(f"YOU LOST. GAME OVER! The correct number was {secret_number}.")`

-----------------

### Activity 6: Basic Calculator

#### 1: Create a Basic Calculator that can do Addition, Subtraction, Multiplication and Division in Python.
```Python
# See file `6-basic-two-number-calculator.py` for code

"""
Sample output:-

Enter the first number: 3.54
Enter the second number: 93.2
Enter an operator (+, -, *, /): +
The result of 3.54 + 93.2 is: 96.74000000000001

Enter the first number: 1
Enter the second number: 0
Enter an operator (+, -, *, /): /
ERROR: Error: Division by zero is not allowed.
"""
```

#### Questions:
**1. How to create choices for the user?**  
**2. How the user input two numbers?**  
Just use `input()` to accept three choices one after another, the two numbers and the operator.

**3. How can you add your define functions inside your If-else statements?**  
There is no need to add a define function inside the if-else statements. If an inline function was needed I'd use a lambda. Was that expected for this solution?

**4. How do stop the calculations at a certain part?**  
I'm not sure what this means or why it would be necessary. Better requirements would help.

**5. How do you cope with this when a user will type a invalid input?**  
The simplest way is raising a suitable error inside the calculation function then catching it outside and showing it then asking the user to re-enter all the inputs correctly. If "per input" validation is required then writing a simple validation function for numbers and another for the operator and catching any error they return would suffice - in this case we would use 3 different while loops to capture all the input so that a failure on the 2nd/3rd one did not jump back to re-entering all the inputs.

-----------------

### My Notes:
- Overall the activities were very simple and I kept the solutions very simple since the goal of this module is to prove I can write basic Python code to an instructor
- Activity 6 was pretty vague and not well defined so I chose the simplest (laziest?) solution. I could have chosen expression parsing but it was more work than I felt like doing for such a basic module.

`[END OF DOCUMENT]`
