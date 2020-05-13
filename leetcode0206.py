# Problem Link: https://leetcode.com/problems/remove-k-digits/
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        s = ""
        start = 0
        x = len(num) - k - 1
        while x >= 0:
            index = num[start:len(num) - x].index(min(num[start:len(num) - x]))
            s += num[index + start]
            start += index + 1
            x -= 1
        return str(int(s))
