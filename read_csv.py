"""
As a Developer, You need to write a python program file “read_csv.py” in
which you need to write a function that reads the given CSV file
“Task_Training_Data.csv”, fetch the data and only return the Name and
Email of all the entries.
"""
# Step 1:
import csv

with open('/Users/rahul/PycharmProjects/practice/Task_Training_Data .csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            print(f'\t{row[0]} | {row[1]}')
            line_count += 1
        else:
            print(f'\t{row[0]} | {row[1]}')
            line_count += 1
    # print(f'Processed {line_count} lines.')
