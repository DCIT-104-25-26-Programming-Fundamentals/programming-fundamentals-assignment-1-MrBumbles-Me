def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))
            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Please enter exactly {cols} values.")
    return matrix


def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


def multiply_matrices(matrixA, matrixB):
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    colsB = len(matrixB[0])

    result = []

    for i in range(rowsA):
        row = []
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += matrixA[i][k] * matrixB[k][j]
            row.append(total)
        result.append(row)

    return result


print("PART A - TRANSPOSE MATRIX")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix:")
matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

print("\nTransposed Matrix:")
transpose = transpose_matrix(matrix)
display_matrix(transpose)

print("\nPART B - ADD TWO MATRICES")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter Matrix 1:")
matrix1 = read_matrix(rows, cols)

print("Enter Matrix 2:")
matrix2 = read_matrix(rows, cols)

print("\nMatrix 1:")
display_matrix(matrix1)

print("\nMatrix 2:")
display_matrix(matrix2)

print("\nSum of Matrices:")
sum_matrix = add_matrices(matrix1, matrix2)
display_matrix(sum_matrix)

print("\nPART C - MULTIPLY TWO MATRICES")

rowsA = int(input("Enter number of rows for Matrix A: "))
colsA = int(input("Enter number of columns for Matrix A: "))

print("Enter Matrix A:")
matrixA = read_matrix(rowsA, colsA)

rowsB = int(input("Enter number of rows for Matrix B: "))
colsB = int(input("Enter number of columns for Matrix B: "))

if colsA != rowsB:
    print("\nMatrix multiplication is not possible.")
    print("The number of columns in Matrix A must equal the number of rows in Matrix B.")
else:
    print("Enter Matrix B:")
    matrixB = read_matrix(rowsB, colsB)

    print("\nMatrix A:")
    display_matrix(matrixA)

    print("\nMatrix B:")
    display_matrix(matrixB)

    print("\nProduct of Matrices:")
    product = multiply_matrices(matrixA, matrixB)
    display_matrix(product)
