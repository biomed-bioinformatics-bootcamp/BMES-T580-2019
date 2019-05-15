# Module 7: A web of images

## Learning Objectives:

### Understanding basic programming concepts
 - How to download image data from the web
 - Basic file/directory CRUD in Python
 - Troubleshooting 3rd party libraries
  
## PreClass Assignment

1. Complete the [LOLCat Factory](https://github.com/biomed-bioinformatics-bootcamp/python-jumpstart-course-demos/tree/master/apps/06_lolcat_factory) assignment from PJS.
  - Check-in and Push the changes to your local repository
  - Check-in and Push a screenshot of you running the code
 
## Assignment (due 7/17/19)

Collecting a large directory of diverse images is an important first step in image processing tasks.
Google Image search is a convienant way to collect images to debug algorithms.
The goal of this project is to make small tool that can download a small collection of histology slides from multiple regions.
Write a program that has the following features.

1. It asks the user for a path to a file CSV file that contains 2 columns.
  - BodyRegion
  - SearchTerm
2. The program reads the file using the csv module. 
3. It uses [Google Images Download](https://github.com/hardikvasa/google-images-download) tool to search using the SearchTerm field.
4. It then downloads the first 10 images and saves them as *BodyRegion*-01,*BodyRegion*-02, ... *BodyRegion*-10 
5. It then does this for all lines in the file.

Create a csv file that has at least 10 different body regions with search terms that will return histology images.

```
BodyRegion,SearchTerm
Brain,neuron histology
Kidney,nephron histology
...
```



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

