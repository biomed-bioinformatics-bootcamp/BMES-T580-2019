import csv
import os

def main():

    print_the_header()

    filename = get_filename()

    age_min, age_max = get_age_cutoff()

    num_pats = 0

    # Open file and start reader
    with open(filename) as handle:
        reader = csv.DictReader(handle)

        for row in reader:
            pat_age = int(row['AGE'])

            # Seperate out the long logic for clarity
            match_age = (pat_age > age_min) and (pat_age < age_max)

            if match_age:
                num_pats += 1

    print('Based on the following criteria:')
    print(' - Age: [%i, %i]' % (age_min, age_max))

    print('There are %i eligible patients' % num_pats)








def print_the_header():
    print('---------------------------------')
    print('       Process Demographics')
    print('---------------------------------')
    print()


def get_filename():

    filename = None
    while filename is None:

        filename = input('What is the /path/to/the/file? ')

        # Check if the filename exists.
        if not os.path.exists(filename):
            print('That file could not be found. Try again.')
            filename = None

    return filename

def get_age_cutoff():

    age_min, age_max = None, None
    while age_min is None:
        age_inp = input('What is the youngest age for the study? ')
        try:
            age_min = int(age_inp)
        except ValueError:
            print(age_inp + ' is not a number. Please try again')
            continue

        if age_min < 18:
            print('Ethics boards require special permission for youth cohort. Please pick an older age')
            age_min = None

    while age_max is None:
        age_inp = input('What is the oldest age for the study? ')
        try:
            age_max = int(age_inp)
        except ValueError:
            print(age_inp + ' is not a number. Please try again')
            continue

    return age_min, age_max


if __name__ == '__main__':
    main()