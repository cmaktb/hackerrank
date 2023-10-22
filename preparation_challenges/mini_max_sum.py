#!/bin/python3

"""
problem:
Given five positive integers,
find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.


example:

Sample Input
1 2 3 4 5

Sample Output
10 14

"""


def miniMaxSum(arr) -> None:
    arr.sort()
    min_sum, max_sum = 0, 0
    for item in arr[:4]:
        min_sum += item

    for item in arr[1:5]:  # or arr[1:]
        max_sum += item

    print(f'{min_sum} {max_sum}')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
