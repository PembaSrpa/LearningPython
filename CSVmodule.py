# Demonstrates reading and writing CSV files

import csv

with open('names.csv', 'r') as csv_file:
    # csv_reader = csv.reader(csv_file)
    # next(csv_reader)  # Skip header
    # for line in csv_reader:
        # print(line)
        # print(line[2])

    csv_reader = csv.DictReader(csv_file)  # Read as dictionary

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        # csv_writer = csv.writer(new_file, delimiter='-')
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()  # Write header

        for line in csv_reader:
            del line['email']     # Remove unwanted field
            csv_writer.writerow(line)

with open('new_names.csv', 'r') as csv_file2:
    csv_reader2 = csv.reader(csv_file2, delimiter='\t')

    for line in csv_reader2:
        print(line)
