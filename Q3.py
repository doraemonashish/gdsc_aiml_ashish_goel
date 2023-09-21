def multiply_matrices(matrix1, matrix2):
    n = len(matrix1)
    result_matrix = [[0] * n for t in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result_matrix[i][j] += matrix1[i][k] + matrix2[k][j]
    return result_matrix

def calculate_trace(matrix):
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    return trace


n = int(input().strip())
matrix1 = [[int(x) for x in input().strip().split()] for i in range(n)]
matrix2 = [[int(x) for x in input().strip().split()] for i in range(n)]

result_matrix = multiply_matrices(matrix1, matrix2)

print("Resultant Matrix: ")
for row in result_matrix:
    print(' '.join(map(str, row)))
trace_result_matrix = calculate_trace(result_matrix)
print("Trace of the Resultant Matrix: ", trace_result_matrix )