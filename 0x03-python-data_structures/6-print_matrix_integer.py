#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers
    ...

    Parameters
    ----------
    matrix : list (of lists)
        The list to print

    Return:
        None
    """

    for row in range(len(matrix)):
        for num in range(len(matrix[row])):
            print("{:d}".format(matrix[row][num]), end="")
            if num != (len(matrix[row]) - 1):
                print(" ", end="")
        print("")
