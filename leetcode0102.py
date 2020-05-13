# Problem Link: https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel = set(J)
        stone = set(S)
        c = 0
        for i in jewel:
            c += S.count(i)
        return c