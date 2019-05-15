# Module 5: Getting that data

## Learning Objectives:

### Understanding basic programming concepts
 - Installing non-native Python modules
 - Interacting with web-services using the `request` module
 - Handling errors during runtime
 - Implementing basic input validation
 
### Basic data processing concepts
 - Parsing data from HTML with `BeautifulSoup`
 - Reading data from CSV files
 - Converting data types
 
## PreClass Assignment

1. Complete the [Weather Client](https://github.com/biomed-bioinformatics-bootcamp/python-jumpstart-course-demos/tree/master/apps/05_weather_client) assignment from PJS.
  - Check-in and Push the changes to your local repository
  - Check-in and Push a screenshot of you running the code
 
## Assignment (due 7/10/19)

This directory contains a `.csv` file containing a simulated list of patients and along with demographic information.
The goal of this project is to make small tool that can create study-groups of patients for downstream analysis.
Write a program that has the following features.   

1. It asks the user for the name of the file for processing.
2. It asks the user for inclusion/exclusion criteria for Age, On Therapy, Length of Infection, etc.
3. It uses input validation techniques for each inclusion/exclusion criteria
4. The file uses the [csv module](https://docs.python.org/3/library/csv.html) to read the file.
5. The program counts the number of patients based on the inclusion/exclusion criteria. 
6. Print the total count of patients that match the criteria.
7. Outputs a new file that contains only the record of patients that match the criteria.


## Rubric

### PJS Grade:

|  Rubric        | Score | 
|----------------|-------|
| Working Code   |  -/5  |
| PEP8 Compliant |  -/5  |
| Comments       |  -/5  |
| Screenshot     |  -/5  |
| On Time        |  -/5  |

### Data Processing:

|  Rubric        | Score | 
|----------------|-------|
| Working Code   |  -/5  |
| PEP8 Compliant |  -/5  |
| Comments       |  -/5  |
| Screenshot     |  -/5  |
| On Time        |  -/5  |

*Final Grade: -/50*

## Resources Used

- Python `request` module discussion https://realpython.com/python-requests/
- `BeautifulSoup` module documentation https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 