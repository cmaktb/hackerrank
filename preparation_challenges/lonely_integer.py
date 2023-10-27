# !/bin/python3
"""
problem: lonely integer

Given an array of integers, where all elements but one occur twice, find the unique element.

Example
a = [1, 2, 3, 4, 3, 2, 1]
The unique element is 4

"""

def lonelyinteger(a):
    unique = 0
    for num in a:
        unique = unique ^ num

    return unique


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)
    print(result)
