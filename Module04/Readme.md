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
2. Do a code-review of your partner's Pregnancy Wheel using the Github editor.
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
 
Use Github's web-editing function to make comments in your partner's Journal App. Remember `# starts comment lines` in Python. 
After your partner has commented on your code you will need to download the newly created branch.
Use the command `git fetch origin *branch_name*`, this will download the new branch into the local repository.
Then using `git checkout *branch_name*` will change the working-directory to the new changes.
In this way your original code stays unchanged while you address these comments.

After you've made the changes commit and then use `git push origin *branch_name*`. 
This will move those changes back up to Github. Use the `@github_name` of your partner to alert them to your new changes.
Once your partner confirms these changes, this may take more than one round of comments, it is time to merge the changes into your master branch.
 
On your local copy checkout the master branch using `git checkout master`. 
You should see that all of the changes you made will disappear. DON'T PANIC.
Now, we merge the changes from that branch into your master using `git merge *branch_name*`.
After the merge, check the files to make sure everything came along. 
Then commit and push using `git push origin master`.

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

- Datetime module: https://docs.python.org/3/library/datetime.html
- Wikipedia explanation on calculating due-dates: https://en.wikipedia.org/wiki/Estimated_date_of_delivery


[^1]: Bergsjø P, Denman DW 3rd, Hoffman HJ, Meirik O. (1990). "Duration of human singleton pregnancy. A population-based study". Acta Obstet Gynecol Scand: 197–207.