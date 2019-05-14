# Module 3: Fun with dates


## Learning Objectives:

- Utilizing a simple Git workflow
 - Editing Readme files
 - Checking in/out code
 - Pushing and Pulling code to/from a repository
 - Accepting & merging Pull Requests
- Understanding basic programming concepts
 - How to encapsulate reusable code into _functions_
 - How to keep related information together using _objects_
 - How to access and change object information using _attributes_ and _methods_.
 

## PreClass Assignment

1. Complete the [Birthday App](https://github.com/biomed-bioinformatics-bootcamp/python-jumpstart-course-demos/tree/master/apps/03_birthday) assignment from PJS .
  - Check-in and Push the changes to your local repository
  - Check-in and Push a screenshot of you running the code
 
## Assignment (due 7/3/19)

1. Check-in and Push code from Module 0 and the pre-class.
2. Accept Pull-Request with your grades from the previous assignment.
3. Complete the Pregnancy wheel assignment described below.
  - Check-in and Push the changes to pregnancy_wheel.py
  - Check-in and Push a screenshot of you using the pregnancy_wheel.py tool.
  - Place the screenshot in this Readme.md file so it properly displays.
  - Add links to any resources used. This includes results of google-searches, Stack-Overflow posts, blog-posts, etc.
4. Add a link to the repo to BBLearn as your "Assignment".

### Pregnancy Wheel

Estimating the gestational age of a fetus is a critical first step in caring for newly pregnant women.
The simplest way to do this is by calculating using the last normal menstrual period (LMP).
Using this along with a 1990 study [^1] of 427,581 Swedish women that found that the average delivery was 281 +/- 13 days after LMP one can calculate the delivery date.

Make a program using the [Birthday App](https://github.com/biomed-bioinformatics-bootcamp/python-jumpstart-course-demos/tree/master/apps/03_birthday) as a template and create `pregnancy_wheel.py`  file in the `Module03` directory.
Modify the code to have the following features.

  - Change the user input prompts to ask for the LMP.
  - Display the estimated gestational age in weeks.
  - Display the due date range using the 281 day offset and the 13 day standard deviation.

## Rubric

### PJS Grade:

|  Rubric        | Score | 
|----------------|-------|
| Working Code   |  -/5  |
| PEP8 Compliant |  -/5  |
| Comments       |  -/5  |
| Screenshot     |  -/5  |
| On Time        |  -/5  |

### Pregnancy Wheel:

|  Rubric        | Score | 
|----------------|-------|
| Working Code   |  -/5  |
| PEP8 Compliant |  -/5  |
| Comments       |  -/5  |
| Screenshot     |  -/5  |
| On Time        |  -/5  |

*Final Grade: -/50*

## Resources Used

- Datetime module: https://docs.python.org/3/library/datetime.html
- Wikipedia explanation on calculating due-dates: https://en.wikipedia.org/wiki/Estimated_date_of_delivery


[^1]: Bergsjø P, Denman DW 3rd, Hoffman HJ, Meirik O. (1990). "Duration of human singleton pregnancy. A population-based study". Acta Obstet Gynecol Scand: 197–207.