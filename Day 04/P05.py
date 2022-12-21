import numpy as np

rows = int(input("Enter count rows: "))
columns = int(input("Enter count columns: "))

def setMatrix(matrix): 
    for row in range(len(matrix)):
        for cell in range(len(matrix[row])):
            matrix[row][cell] = int(input("Enter a number : "))
    
    return matrix

def PlusMatrix(matrix_1, matrix_2):
    matrix_3 = matrix_1 + matrix_2

    return matrix_3

matrix_1 = np.array([[0] * columns] * rows)
matrix_2 = np.array([[0] * columns] * rows)

print(setMatrix(matrix_1))
print(setMatrix(matrix_2))

print(PlusMatrix(matrix_1, matrix_2))