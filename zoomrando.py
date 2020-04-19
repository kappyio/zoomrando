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
my_set = set()

print("There are {0} screens with {1} rows and {2} columns.".format(screens, rows, cols))


while len(my_set) < participants:
    r_scr = random.randint(1, screens)
    r_row = random.randint(1, rows)
    r_col = random.randint(1, cols)
    my_digits = int(str(r_scr) + str(r_row) + str(r_col))
    # print(type(my_digits))
    # print(my_digits)
    my_set.add(my_digits)

print(my_set)
