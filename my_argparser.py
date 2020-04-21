#!/usr/bin/env python3 

import argparse
import math
import random

parser = argparse.ArgumentParser(description='Produce a list of random grid \
                                 coordinates for participants in a zoom meeting. \
                                 Uses Zoom\'s "Gallery View".')
parser.add_argument('participants', type=int, help="How many participants are in the meeting?")
parser.add_argument('rows', type=int, help="How many rows do you see in gallery view?")
parser.add_argument('cols', type=int, help="How many columns do you see in gallery view?")
args = parser.parse_args()

def grid_calc(participants, rows, cols):
    my_list = list()
    screens = (math.ceil(participants / (rows * cols)))
    print("There are {0} participants spread across {1} screens with {2} rows and {3} columns.".format(participants, screens, rows, cols))
    while len(my_list) < participants:
        r_scr = random.randint(1, screens)
        r_row = random.randint(1, rows)
        r_col = random.randint(1, cols)
        my_digits = int(str(r_scr) + str(r_row) + str(r_col))
        print(my_digits)
        if my_digits in my_list:
            continue
        else:
            my_list.append(my_digits)

    return my_list

if __name__ == '__main__':
    l = grid_calc(args.participants, args.rows, args.cols)
    for num in l:
        if len(str(num)) > 3:
            print("Screen: {0}, Row: {1}, Column: {2}".format(str(num)[:2],
                                                              str(num)[2],
                                                              str(num)[3]))
        else:
            print("Screen: {0}, Row: {1}, Column: {2}".format(str(num)[0], str(num)[1], str(num)[2]))

    print(l)
