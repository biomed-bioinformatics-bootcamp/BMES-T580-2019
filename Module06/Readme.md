# Module 6: DNA Analysis

## Learning Objectives:

### Understanding basic programming concepts
 - Object oriented design
 - Using subclassing effectively
 - Adding methods to subclassed objects
 
### Basic biological data processing concepts
 - How to read, parse, and write FASTA formatted sequence files
 - How to handle and process DNA/RNA/Protein data in using BioPython
 - How to transcribe DNA into RNA and how to translate RNA into protein using BioPython 
 
## PreClass Assignment

1. Complete the [Wizard Battle](https://github.com/biomed-bioinformatics-bootcamp/python-jumpstart-course-demos/tree/master/apps/07_wizard_battle) assignment from PJS.
  - Check-in and Push the changes to your local repository
  - Check-in and Push a screenshot of you running the code
 
## Assignment (due 7/14/19)

The goal of this project is to make small tool that can isolate sequences that contain complete Open Reading Frames (ORFs).
Write a program that has the following features.

1. It asks the user for a DNA sequence.
2. It asks the user for a path to write a results file.
3. It searches the sequence for all ORFs.
4. It checks both strands for ORFs.
5. It writes the *translated* amino acid sequences to the file. 
6. It prints summary information about how many sequences it processed and how many ORFs it found.

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

- Python `BioPython` module documentation https://biopython.org/wiki/Documentation
- `BioPython` cookbook http://biopython.org/DIST/docs/tutorial/Tutorial.html
- Reference for common sequence formats https://bioinformatics.uconn.edu/resources-and-events/tutorials-2/file-formats-tutorial/