import numpy as np
""" 
matrix = np.array([
[1,0,0,1,0],
[1,0,1,0,0],
[0,0,1,0,1],
[1,0,1,0,1],
[1,0,1,1,0]
])
"""
"""
After the verification of the user, it must show a welcome note, refer to
“welcome_note.txt” file.
After showing the note It should ask for a choice whether you wanted to
get in or not.
For choice program should take input “Yes” or “No”.
If choice = “Yes”: It should move forward and show the instructions of the
game, refer to “game_instruction.txt”.

If choice = “No”: It should terminate the programm

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
            #print("User found in the database,Move Forward")
            print("""Welcome to the brain game of River and Land : Just Remember what you give"
Quote: This game can boot your Stress or you will be happy , will become a myth
Note: programmer allowed to add their own thoughts""")
            choice = input("Would you like to  get in or not “Yes” or “No”: ").lower()
            if choice =="yes":
                    dd = open("/Users/rahul/PycharmProjects/practice/game_instruction.txt","r")
                    print(dd.read())

                    press_p = input("Press P to Play: ").lower()

                    if press_p == "p":
                        R = int(input("Enter the number of rows:"))
                        C = int(input("Enter the number of columns:"))
                        # Initialize matrix
                        matrix = []
                        print("Enter the entries rowwise:")

                        # For user input
                        for i in range(R):  # A for loop for row entries
                            a = []
                            for j in range(C):  # A for loop for column entries
                                a.append(int(input()))
                            matrix.append(a)
                    # given_matrix = x
                    rows = len(matrix)
                    cols = len(matrix[0])
                    river_length = []


                    def game_func(given_matrix):
                        for i in range(0, rows):
                            for j in range(0, cols):
                                # Checking if the current element is not island
                                if given_matrix[i][j] != 0:
                                    # if the value of top element is river
                                    top_value = given_matrix[i - 1][j] if i - 1 > -1 else 0
                                    left_value = given_matrix[i][j - 1] if j - 1 > -1 else 0
                                    # island_matrix[i][j] = island_matrix[i][j] + island_matrix[i-1][j] + island_matrix[i][j-1]
                                    given_matrix[i][j] = given_matrix[i][j] + top_value + left_value

                                    # if there is river then there is top value and if we already remembered top value then update the given matrix
                                    # as we already noted it
                                    if top_value != 0:
                                        given_matrix[i - 1][j] = 0
                                    if left_value != 0:
                                        given_matrix[i][j - 1] = 0

                        # print(given_matrix)

                        for i in range(0, rows):
                            for j in range(0, cols):
                                if given_matrix[i][j] != 0:
                                    river_length.append(given_matrix[i][j])
                        return (river_length)


                    def user_choice_func():
                        user_choice = []
                        guess = 0
                        for i in range(len(river_length)):
                            u = int(input(f"Enter the guess no {guess}: "))
                            user_choice.append(u)
                            guess = guess + 1
                        # print(user_choice)
                        count = 0
                        for j in range(len(user_choice)):
                            if user_choice[j] == river_length[j]:
                                count = count + 1
                        # print(count)
                        if (count) == len(river_length):
                            print("You are the winner")
                        elif (count) >= round(60 / 100 * len(river_length)):
                            print("You got second position")
                        elif (count) < round(60 / 100 * len(river_length)):
                            print("Invest more money on Almonds, then come back")
                        play_again = input("If you wanted to play again press Yes/No: ").lower()
                        if play_again == 'yes':
                            user_choice_func()
                        else:
                            print("Goodbye,See you again!")
                            exit()

                            # For printing the matrix


                    #   for i in range(R):
                    #      for j in range(C):
                    #         print(matrix[i][j], end=" ")

                    river_length = game_func(matrix)

                    user_choice_func()

            elif choice=="no":
                    print("Exiting the programm")
                    exit()
            found = True
            #exit()
    #if found==True:
      #  exit()
    else:
        print("Incorrect details entered!! you have more {} chances to enter details".format(2 - count))
        count=count+1




