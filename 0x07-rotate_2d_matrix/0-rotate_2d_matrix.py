#!/usr/bin/python3
"""
Matrix Rotation Function
"""


def rotate_2d_matrix(matrix):
    """
    rotate 2d matrix
    """
    mat_len = len(matrix)
    for i in range(mat_len):
        for j in range(i, mat_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(mat_len):
        matrix[i].reverse()
