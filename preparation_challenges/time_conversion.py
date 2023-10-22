#!/bin/python3

"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

example:

Sample Input
07:05:45PM

Sample Output
19:05:45

"""

from datetime import datetime


def timeConversion(s) -> str:
    my_time = datetime.strptime(s, "%I:%M:%S%p")
    converted_time = datetime.strftime(my_time, "%H:%M:%S")
    return converted_time


if __name__ == '__main__':
    OUTPUT_PATH = 'time.txt'
    fptr = open(OUTPUT_PATH, 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
