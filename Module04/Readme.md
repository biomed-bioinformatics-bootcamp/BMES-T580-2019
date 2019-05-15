# Module 4: Journaling your progress

## Learning Objectives:

### Understanding basic programming concepts
 - Safely opening and closing files
 - How to iterate over file lines using for-loops
 - How to save strings to a file

### Basic code review techniques
 - Understand the advantages and disadvantage of code-review
 - How to use Github for easy code review
 - How to create git branches
 - How to merge branches
 - Perform a code-review a fellow student
 - How to change your code in response to a peer-review
 
## PreClass Assignment

1. Complete the [Journal App](https://github.com/biomed-bioinformatics-bootcamp/python-jumpstart-course-demos/tree/master/apps/04_journal) assignment from PJS .
  - Check-in and Push the changes to your local repository
  - Check-in and Push a screenshot of you running the code
  - Check-in your journal file.
 
## Assignment (due 7/7/19)

1. Choose a partner (or group of 3) for the assignment.
2. Do a code-review of your partner's Pregnancy Wheel by forking as described below.
3. Merge the code-review comments into your own repository on a new branch
4. Address the comments in the new branch with additional commits
5. Push the new branch to Github and re-review the edits with your partner
6. After you both agree on the edits, merge the branch with `master`.
7. Post a screen shot of the Github code review to BBLearn as your assignment.  

### Code Review

I have summarized much of this content from this [Medium article](https://medium.com/palantir/code-review-best-practices-19e02780015f). 
Please read the source for additional context.
 
Reviewing code is a critical step to any programming project.
Whether you are working by yourself or on a team it is important to ensure that code is correct, legible, and efficient.
The best way to do this is to perform regular code reviews while the changes are fresh.

This week we will perform peer code reviews in pairs.
It is important to remember that this is a constructive learning opportunity and not an adversarial process or braggadocious contest.
Each organization has its own code process but they all share the same basic style.
We'll focus our reviews on four main areas:

1. Purpose
2. Implementation
3. Legibility & Style 
4. Maintainability

In addition to the points mentioned in the Medium article linked above, look out for these common problems.
- Short and non-descriptive variable names like `i`, `j`, `num`, `tmp`, etc.
- Inconsistent variable style. Ie alternating between `under_scores` and `camelCase` variables.
- Functions without docstrings
- Docstrings missing input/output variable descriptions
- Lines that are too long 
- Complex programming logic
 
For this code-review I want you to both make the comment AND fix the issue.
If the variable names are non-descriptive, make the comment, and replace them with more descriptive ones.
If the lines are too long, make the comment, and adjust them to be shorter.
For this excercise, focus on improving legibility.
Most importantly, the code needs to run after the changes! Don't break someone else's code.

### Git Workflow

I have summarized much of this content the Git explainers referenced in the notes section. 
Please read the source for additional context.
If you Google around on your own, which I highly encourage, you will find 4 common Git workflows. 
To avoid confusion please stick to explanations of the "Feature Branch" workflow.
I've added links to the relevant parts below. 
I've also split this explanation up based on your current role in the review process.

*Reviewer*
  1. Use Github's tools to create a fork of your partner's repo.
  2. Clone that repo to a NEW directory.
  3. Create a new branch using `git checkout -b wheel_code_review`
  4. Use Pycharm to add comments and improve the code.
  5. Commit as usual.
  6. Push to a new remote branch using `git push origin wheel_code_review`
  7. Github should now give you an option to create a new Pull Request. [Like this](https://gist.github.com/vlandham/3b2b79c40bc7353ae95a#create-pull-request)
  8. In the comments on the Pull Request post a screenshot of the working code.
  
*Developer*
Github's tools make reviewing and accepting a Pull Request easy. 
This helps project maintainers coordinate a streamlined workflow.
  1. Github processes the Pull Request, you should get an email and your Repo homepage will change a bit ([Read more](https://gist.github.com/vlandham/3b2b79c40bc7353ae95a#finding-pull-requests)).
  2. If the Pull Request is acceptable you can use Github's tools to automaticall merge everything.


## Rubric

### PJS Grade:

|  Rubric        | Score | 
|----------------|-------|
| Working Code   |  -/5  |
| PEP8 Compliant |  -/5  |
| Comments       |  -/5  |
| Screenshot     |  -/5  |
| On Time        |  -/5  |

### Code Review:

|  Rubric        | Score | 
|----------------|-------|
| Review of partner's code   |  -/20  |
| Addressing your partner's comments on your code |  -/20  |
| Prompt responses to clarifications  |  -/10  |
| Professionalism during the process | -/10

*Final Grade: -/100*

## Resources Used

- General walkthrough of the Feature Branch git strategy https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud
- Walkthrough of Github specific actions https://gist.github.com/vlandham/3b2b79c40bc7353ae95a#finding-pull-requests