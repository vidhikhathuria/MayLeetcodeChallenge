# Problem Link : https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a = 0
        b = 0
        ans = []
        while a != len(A) and b != len(B):
            x = max(A[a][0], B[b][0])
            y = min(A[a][1], B[b][1])
            if x <= y:
                ans.append([x, y])
            # print(A[a][1], B[b][1])
            if max(A[a][1], B[b][1]) == A[a][1]:
                b += 1
            else:
                a += 1
        return ans