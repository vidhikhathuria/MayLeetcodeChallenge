# Problem Link: https://leetcode.com/problems/find-the-town-judge/
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and len(trust) == 0:
            return N
        li = [x for x in range(1, N + 1)]
        hashMap = {}
        for i in trust:
            if i[0] in li:
                li.remove(i[0])
            if i[1] not in hashMap:
                hashMap[i[1]] = 1
            else:
                hashMap[i[1]] += 1
        if len(li) == 1 and li[0] in hashMap and hashMap[li[0]] == N - 1:
            return li[0]
        else:
            return -1