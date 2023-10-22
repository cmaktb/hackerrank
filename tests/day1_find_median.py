#!/bin/python3
"""
find median function for an array with odd length
"""
OUTPUT_PATH = 'findMedian.txt'


def findMedian(arr):
    arr.sort()
    middle_index = len(arr) // 2
    median = arr[middle_index]
    return median


if __name__ == '__main__':
    fptr = open(OUTPUT_PATH, 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
