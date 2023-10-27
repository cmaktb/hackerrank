"""
Problem:
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

"""

"""
This is the answer with numpy library.(it's much easier this way)
# import numpy as np
#
# a = [[2, 3, 5],
#      [1, 4, 6],
#      [6, 8, 9]]
#
# v = np.array(a)
# vd1 = v.diagonal()
#
# v2 = np.fliplr(v)
# vd2 = v2.diagonal()

"""
#

def diagonalDifference(arr):
    sum_diagonal_lr, sum_diagonal_rl = 0, 0
    arr_length = len(arr)
    for i in range(len(arr)):
        sum_diagonal_rl += arr[i][i]
        sum_diagonal_lr += arr[i][arr_length - i-1]

    return abs(sum_diagonal_lr - sum_diagonal_rl)


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
