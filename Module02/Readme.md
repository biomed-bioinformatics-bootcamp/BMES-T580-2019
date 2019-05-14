# Module 2: Guessing Games


## Learning Objectives:

- Utilizing a simple Git workflow
 - Editing Readme files
 - Checking in/out code
 - Pushing and Pulling code to/from a repository
 - Accepting & merging Pull Requests
- Understanding basic programming concepts
 - Loops
 - Basic user input
 - Conditionals and Booleans
 - Basic string indexing


## PreClass Assignment

1. Complete the Guess that number assignemnt from PJS.
  - Check-in and Push the changes to your local repository
  - Check-in and Push a screenshot of you playing the game
 
## Assignment (due 6/30/19)

1. Check-in and Push code from Module 0 and the pre-class.
2. Accept Pull-Request with your grades from the previous assignment.
3. Complete the Primer Guessing assignment described below.
  - Check-in and Push the changes to guess_my_primer.py
  - Check-in and Push a screenshot of you playing the Guess A Primer game.
  - Place the screenshot in this Readme.md file so it properly displays.
  - Add links to any resources used. This includes results of google-searches, Stack-Overflow posts, blog-posts, etc.
3. Add a link to the repo to BBLearn as your "Assignment".

### Guess A Primer

Dozens of molecular biology techniques use oligigonucleotide primers as fundemental tools to answer bioligical questions.
These primers consist of short segments (15-45bp) of single-stranded DNA that researchers use to create short double-stranded segments of initially single-stranded DNA. 
In order for this annealing to happen, they must identically match the target sequence *(technically it must match the reverse-complement, but we'll deal with that in Module 6)*.

Make a program using the [Guess That Number](https://github.com/biomed-bioinformatics-bootcamp/python-jumpstart-course-demos/tree/master/apps/02-guess-number-app) as a template and make a `guess_that_primer.py` file in the `Module02` directory.
Modify the code to have the following features.

  - Replace the "guess a number" code with something that generates a random DNA string. Make the string 5 letters long.
  - Provide the user with the number letters to guess.
  - Check the user input against the target DNA string.
    - If the user guesses correctly. Print a congrats and exit.
    - If the user guesses incorrectly, Print the number of correct letters. Then allow another guess.

## Rubric

### PJS Grade:

|  Rubric        | Score | 
|----------------|-------|
| Working Code   |  -/5  |
| PEP8 Compliant |  -/5  |
| Comments       |  -/5  |
| Screenshot     |  -/5  |
| On Time        |  -/5  |

### Guess A Primer Grade:

|  Rubric        | Score | 
|----------------|-------|
| Working Code   |  -/5  |
| PEP8 Compliant |  -/5  |
| Comments       |  -/5  |
| Screenshot     |  -/5  |
| On Time        |  -/5  |

*Final Grade: -/50*

## Resources Used

- Random choices from lists: https://docs.python.org/2/library/random.html#random.choice