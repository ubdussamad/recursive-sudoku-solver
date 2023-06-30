import math
import time
import random
import sys
import os


def read_file(filename):
    matrix = []
    with open("puzzle.csv", "r") as f:
        buffer = f.read()
        rows = buffer.split("\n")
    
        for row in rows:
            _tmp = []
            cols = row.split(",");
            for col in cols:
                _tmp.append(int(col))
            matrix.append(_tmp)
    return matrix



# This function could be the recursive one or you can make others.
def solve(x,y,matrix):
    pass

# Given a cell's index (row, col) in the 2D array, it'll return all possible numbers which can be filled in that cell.
def list_possibilities(row_index,col_index, matrix):
    # Cell :
    #  We check the row and the column for numbers.
    # x: 0 , y: 0
    # row_index
    # Check horizontally
    array = [i for i in range(1,10)]
    for i in range(8):
        element = matrix[row_index][i]
        if element in array:
            array.pop(array.index(element))
    
    for j in range(8):
        element = matrix[i][col_index]
        if element in array:
            array.pop(array.index(element))
    # H/W. do the block thing.
    pass

# Just to take a look at the matrix before and after it's solved.
def print_matrix(matrix):
    for i in matrix:
        print(i)
        

def main():
    # Read the file
    mat = read_file("puzzle.csv")
    print(mat)
    # Solve the problem
    # Print the solution
    print_matrix(mat)
    
    pass

if __name__ == "__main__":
    main()

