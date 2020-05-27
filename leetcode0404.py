# Problem Link : https://leetcode.com/problems/uncrossed-lines/

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        li = [[0 for i in range(len(B) + 1)] for j in range(len(A) + 1)]
        # for i in li:
        #     print(i)
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    li[i + 1][j + 1] = li[i][j] + 1
                else:
                    li[i + 1][j + 1] = max(li[i][j + 1], li[i + 1][j])
        return li[-1][-1]
        