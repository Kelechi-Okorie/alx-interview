#!/usr/bin/python3
"""
Pascals triangle implementation
"""


def pascal_triangle(n):
    """
    Returns the pascal triangle for a given value.

    Parameters:
    - n (int): The number for which the pascal's triangle will be generated.

    Returns:
    - list of lists: The pascal triangle generated.
    """

    triangle = []

    if n <= 0:
        return triangle

    triangle.append([1])

    for i in range(1, n):
        temp = [1]
        for j in range(1, i):
            s = triangle[i-1][j-1]
            t = triangle[i-1][j]
            temp.append(s+t)
        temp.append(1)
        triangle.append(temp)
    return triangle
