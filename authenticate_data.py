"""
#Step 2:
Write a separate python file “authenticate_data.py” in which the program
takes Name and Email from the user as input and matches the data
returned from the first read_csv.py file that is Name and Email.
If Name and Email Matches with the data returned from “read_csv.py”
then the user is allowed to move forward otherwise it should give
maximum two chances and after 2 wrong attempts, it should exit.
"""

import csv
my_dict = {}
x=0
with open('/Users/rahul/PycharmProjects/practice/Task_Training_Data .csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    for row in csv_reader:
        my_dict.update({ x:(({A.strip():N.strip() for (A,N) in [x for x in row.items()] [:2]}))})
        x=x+1
    count=1

found=False
count=0
while count<3:
    print(my_dict)
    nm = input("enter the name: ")
    nb = input("enter the email: ")
    for key, value in my_dict.items():
        if value['Name']== nm and value['Email']== nb:
            print("User found in the database,Move Forward")
            found= True
            exit()
    if found==True:
        exit()
    else:
        print("Incorrect details entered!! you have more {} chances to enter details".format(2 - count))
        count=count+1



