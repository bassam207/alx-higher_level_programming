#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_list = []

    for row in matrix:
        squared_row = []

        for num in row:
            squared_row.append(num ** 2)
        squared_list.append(squared_row)
    return (squared_list)
