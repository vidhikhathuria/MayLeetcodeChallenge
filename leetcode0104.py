# Problem Link: https://leetcode.com/problems/number-complement/
class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num).replace("0b", "")
        s = ''
        for i in num:
            if i == '0':
                s += '1'
            else:
                s += '0'
        return int(s,2)

