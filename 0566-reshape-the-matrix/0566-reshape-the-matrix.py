class Solution:
    def matrixReshape(self, mat: List[List[int]], rows: int, cols: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != rows * cols:
            return mat
        elements = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                elements.append(mat[i][j])
        matrix = []
        for i in range(rows):
            row = elements[i*cols:(i+1)*cols]
            matrix.append(row)
        return matrix
