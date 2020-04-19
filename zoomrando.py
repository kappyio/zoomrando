import random
import math

# TODO
# prompt, or run with args
# Make sure an int is entered
# Limit to n participants (300)
# Make into a web page people can go to to use


participants = 146
rows = 5
cols = 4
screens = (math.ceil(participants / (rows * cols)))

# r_participants = input("How many partcipants are there? ")
# r_row = input("How many rows are there? ")
# r_col = input("How many columns are there? ")
# my_set = set()
my_list = list()

print("There are {0} participants spreade across {1} screens with {2} rows and {3} columns.".format(participants, screens, rows, cols))


while len(my_list) < participants:
    r_scr = random.randint(1, screens)
    r_row = random.randint(1, rows)
    r_col = random.randint(1, cols)
    my_digits = int(str(r_scr) + str(r_row) + str(r_col))
    # print(my_digits)
    if my_digits in my_list:
        continue
    else:
        my_list.append(my_digits)

# print("This meetings has {0} participants.".format(len(my_list)))

# print(my_list)

for num in my_list:
    print("Screen: {0}, Row: {1}, Column: {2}".format(str(num)[0], str(num)[1], str(num)[2]))
