#!/bin/python3
"""
Problem:
Counting sort frequency array

"""


def countingSort(arr):
    max_value = max(arr)
    frequency_arr = [0] * (max_value + 1)

    for num in arr:
        frequency_arr[num] += 1

    return frequency_arr


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    print(result)
