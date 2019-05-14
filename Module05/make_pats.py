import random
import csv

if __name__ == '__main__':

    # Set a seed for reproducible randomness
    random.seed(123456789)

    #Open the new file
    with open('pat_data.csv', 'w') as handle:

        # Make the writer and start the file
        fields = ['PAT_NUM', 'SEX',
                  'AGE', # in years
                  'INFECTION_LENGTH', # in years
                  'ON_THERAPY', 'COINFECTION', #Yes/No
                  ]
        writer = csv.DictWriter(handle, fields, delimiter = ',')
        writer.writeheader()

        for n in range(10000):

            # Make up a patient as a dict
            age = random.randint(18, 80)
            pat_info = {'PAT_NUM': n,
                        'SEX': random.choice(['Male', 'Female']),
                        'AGE': age,
                        'INFECTION_LENGTH': random.randint(0, age), #can't be infected more than Age
                        'ON_THERAPY': random.choices(['Yes', 'No'], weights = [0.8, 0.2])[0], #returns list ['Yes']
                        'COINFECTION': random.choices(['Yes', 'No'], weights = [0.6, 0.4])[0],
                        }

            writer.writerow(pat_info)