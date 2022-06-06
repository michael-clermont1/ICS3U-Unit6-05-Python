#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: June 2022
# This program calculates the average using lists

import random


def average_of_numbers(allmarks):
    # this function gets the average

    numbers_average = 0
    for singlemark in allmarks:
        numbers_average = singlemark + numbers_average
    numbers_average = numbers_average / len(allmarks)

    return numbers_average


def main():
    # this function gets the marks

    marks = []

    # input
    mark = int(input("What is your mark? (as %): "))
    marks.append(mark)
    while mark != -1:
        if mark > 100 or mark < -1:
            marks.pop()
            mark = int(input("That is not a valid mark, enter another mark! (as %): "))
            marks.append(mark)
        mark = int(input("What is your mark? (as %): "))
        marks.append(mark)
    marks.pop()
    print("")

    average = average_of_numbers(marks)
    print("The average is: {0}%.".format(average))


if __name__ == "__main__":
    main()
