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
Sample output (in this case I passed no args via command line and used the defaults):-

./large-file-renamer.py
File Renaming Sample Project

Usage: usage: large-file-renamer.py [-h] [--in_dir IN_DIR] [--out_dir OUT_DIR] [--pattern PATTERN]

Bulk rename files in a directory.

options:
  -h, --help         show this help message and exit
  --in_dir IN_DIR    The path to the directory containing files to rename. Default is './sample_files'.
  --out_dir OUT_DIR  The path to the directory where renamed files will be saved. Default is './renamed_sample_files'.
  --pattern PATTERN  The renaming pattern. Use {name} for original name, {ext} for extension, and {num} for a sequential number. Default is 'renamed_{num}_{name}.{ext}'.

Arguments: {
    "in_dir": "./sample_files",
    "out_dir": "./renamed_sample_files",
    "pattern": "renamed_{num}_{name}.{ext}",
    "in_dir_safe": "/Development/future-connect-training/fc-python-projects/5-large-file-renamer/sample_files",
    "out_dir_safe": /Development/future-connect-training/fc-python-projects/5-large-file-renamer/renamed_sample_files"
} 

Renaming files
  * From: /Development/future-connect-training/fc-python-projects/5-large-file-renamer/sample_files
  * To: /Development/future-connect-training/fc-python-projects/5-large-file-renamer/renamed_sample_files
  * Pattern: renamed_{num}_{name}.{ext}

Copy: not_a_sample.md -> renamed_1_not_a_sample.md
File copied successfully.
Copy: sample_2.txt -> renamed_2_sample_2.txt
File copied successfully.
Copy: sample_3.txt -> renamed_3_sample_3.txt
File copied successfully.
Copy: sample_1.txt -> renamed_4_sample_1.txt
File copied successfully.
"""
```

#### Notes:
- I thought about this one and considered several approaches (I decided to do #2):
  1. Just allow entry of a path and list the files and rename them using os.rename according to a hard coded algorithm
	2. Create a more CLI tool which accepts args and will create a copy of the original file with a new name in a new folder (safer)
- Since entering in paths is pretty risky for security reasons I decided to restrict the in_path and out_path to folders in the script folder
- Because I chose the safer approach I ended up using a file copy instead of os.rename

-----------------

### Project 6: Web Scraping

#### The task is to scrape the list of largest companies in US by revenue form wikipedia using Beautiful Soup in Python. The data required to be extracted includes the Rank, Name of company, Industry, Revenue, Revenue growth, Headquarters for the top US companies by revenue.
```Python
# See folder `6-web-scraping` for my code

"""
Sample output (first 30 rows out of 100):-

Web Scraping: Largest Companies in the US by Revenue

rank                                name                           industry revenue_usd_millions revenue_growth employees                               headquarters
   1                             Walmart                             Retail              680,985           5.1% 2,100,000                      Bentonville, Arkansas
   2                              Amazon          Retail andcloud computing              637,959          11.0% 1,556,000                        Seattle, Washington
   3                  UnitedHealth Group                         Healthcare              400,278           7.7%   400,000                      Minnetonka, Minnesota
   4                               Apple                         Technology              391,035           2.0%   164,000                      Cupertino, California
   5                          CVS Health                         Healthcare              372,809           4.2%   259,500                   Woonsocket, Rhode Island
   6                  Berkshire Hathaway                       Conglomerate              371,433           1.9%   392,400                            Omaha, Nebraska
   7                            Alphabet      Technologyand cloud computing              350,018          13.9%   183,323                  Mountain View, California
   8                         Exxon Mobil                 Petroleum industry              349,595           1.5%    60,900                              Spring, Texas
   9                McKesson Corporation                         Healthcare              308,951          11.7%    48,000                              Irving, Texas
  10                             Cencora                 Pharmacy wholesale              293,959          12.1%    44,000                 Conshohocken, Pennsylvania
  11                      JPMorgan Chase                         Financials              278,906          16.5%   317,233                    New York City, New York
  12                    Costco Wholesale                             Retail              254,453           5.0%   333,000                       Issaquah, Washington
  13                               Cigna                   Health insurance              247,121          26.6%    72,398                    Bloomfield, Connecticut
  14                           Microsoft     Technology and cloud computing              245,122          15.7%   228,000                        Redmond, Washington
  15                     Cardinal Health                         Healthcare              226,827          10.6%    48,411                               Dublin, Ohio
  16                             Chevron                 Petroleum industry              202,792           0.9%    45,298                             Houston, Texas
  17                     Bank of America                         Financials              192,434          11.9%   213,193                  Charlotte, North Carolina
  18                      General Motors                Automotive industry              187,442           9.1%   162,000                          Detroit, Michigan
  19                          Ford Motor                Automotive industry              184,992           5.0%   171,000                         Dearborn, Michigan
  20                     Elevance Health                         Healthcare              177,011           3.3%   103,679                      Indianapolis, Indiana
  21                           Citigroup                         Financials              170,757           8.9%   227,855                    New York City, New York
  22                      Meta Platforms                         Technology              164,501          21.9%    74,067                     Menlo Park, California
  23                             Centene                         Healthcare              163,071           5.9%    60,500                        St. Louis, Missouri
  24                          Home Depot                             Retail              159,514           4.5%   470,100                           Atlanta, Georgia
  25                          Fannie Mae                         Financials              152,670           8.1%     8,200                           Washington, D.C.
  26            Walgreens Boots Alliance            Pharmaceutical industry              147,658           6.2%   252,500                        Deerfield, Illinois
  27                              Kroger                             Retail              147,123          -1.9%   409,000                           Cincinnati, Ohio
  28                         Phillips 66                 Petroleum industry              145,496          -2.9%    13,200                             Houston, Texas
  29                  Marathon Petroleum                 Petroleum industry              140,412          -6.6%    18,300                              Findlay, Ohio
  30              Verizon Communications                 Telecommunications              134,788           0.6%    99,600                    New York City, New York
"""
```

#### Notes:
- I decided to just scrape the page and create a simple Pandas data frame to hold the data
- I left the numbers as formatted strings, but I could have easily added more columns to hold numeric versions of the values (eg. revenue_usd_millions_num)
- I decided not to output the Pandas dataset as a CSV file and just print to console, but it's easy to do so once you have the DataFrame

-----------------

### My Notes:
- Overall the projects were very simple and I kept the solutions very simple.
- I could have chosen to use tkinter for displaying UI elements and capturing form but all the projects had very simple needs for user input and none of the projects asked for it to be used.
- I did not end up using the graph plotting library since none of the projects asked for a graph. The most suitable one would have been the web scraping of top US companies by revenue - I could have output a pie chart or bar graph.
- I did not choose to save any of the datasets to a database via sqllite3 since the projects themselves did not ask for it. Either the Zodiac Sign or the the Web Scraping project would have been fine for saving to a database.
- Some feedback: Generally speaking I believe that if a tool is taught then an assignment or project should test the use of that tool. The projects were overall not very well specced and they did not test all the material taught on this module.

`[END OF DOCUMENT]`
