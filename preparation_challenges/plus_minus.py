"""
problem:

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.

example:
Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output

0.500000
0.333333
0.166667
"""


def plusMinus(arr) -> None:
    zero_n = 0
    if 0 in arr:
        zero_n = arr.count(0)

    negative_n = 0
    for item in arr:
        if item < 0:
            negative_n += 1

    positive_n = 0
    for item in arr:
        if item > 0:
            positive_n += 1

    positive_ratio = positive_n / n
    negative_ratio = negative_n / n
    zero_ratio = zero_n / n

    if positive_n != 0:
        print(f'{positive_ratio:0,.6f}')
    else:
        print('0.000000')
    if negative_n != 0:
        print(f'{negative_ratio:0,.6f}')
    else:
        print('0.000000')
    if zero_n != 0:
        print(f'{zero_ratio:0,.6f}')
    else:
        print('0.000000')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
