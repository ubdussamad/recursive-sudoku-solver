import math
import time
import random
import sys
import os



def read_file(filename):
    matrix = []
    with open("success.csv", "r") as f:
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
def solve(row_index,col_index,matrix):
    break_flag = False
    for i in range(9):
        if break_flag == True:
            break
        for j in range(9):
            if matrix[i][j] == 0:
                break_flag = True
                row_index = i
                col_index = j
                break

            else:
                if i == 9 and j == 9:
                    return 1
    
    if break_flag == False: return 1
    possiblities = list_possibilities(row_index,col_index, matrix)
    # array_length = len(possiblities) // 
    
    
    if len(possiblities) == 0:return -1


    


    for k in range(len(possiblities)):
        matrix[row_index][col_index] = possiblities[k]

        if solve(row_index, col_index,matrix) == -1:
            matrix[row_index][col_index] = 0
            continue
        else:
            return 1
    return -1


# Given a cell's index (row, col) in the 2D array, it'll return all possible numbers which can be filled in that cell.
def list_possibilities(row_index,col_index, matrix):
    # Cell :
    #  We check the row and the column for numbers.
    # x: 0 , y: 0
    # row_index
    # Check horizontally
    
    array = [i for i in range(1,10)]
    for i in range(9):
        element = matrix[row_index][i]
        if element in array:
            array.pop(array.index(element))
    
    for j in range(9):
        element = matrix[j][col_index]
        if element in array:
            array.pop(array.index(element))
    
    
    block_row = row_index // 3
    block_col = col_index // 3

    start_row = block_row * 3
    start_col = block_col * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            element = matrix[i][j]
            
            if element in array:
                array.pop(array.index(element))

    return array
# Just to take a look at the matrix before and after it's solved.
def print_matrix(matrix):
    for i in matrix:
        print(i)
        

def main():
    # Read the file
    mat = read_file("success.csv")
    print("The matrix is ............")
    print_matrix(mat)

    print("The solution is.............")
    if solve(0,0,mat) == 1:
        print("Big W!")
        print_matrix(mat)
    else:
        print("Big L!")
        print_matrix(mat)

     # Solve the problem
    # Print the solution
    

    
    
    pass

if __name__ == "__main__":
    main()

