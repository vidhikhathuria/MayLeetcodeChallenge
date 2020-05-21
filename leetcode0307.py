# Problem Link : https://leetcode.com/problems/count-square-submatrices-with-all-ones/


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        s = sum(matrix[0])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])+1
            s += sum(matrix[i])
        return s
