def checkio(matrix):
    matrixLen = len(matrix)
    if matrixLen == 0:
        return []
    tMatrix = [[] for col in matrix[0]]
    for row in range(matrixLen):
        for col in range(len(matrix[row])):
            tMatrix[col].append(matrix[row][col])
    return tMatrix
