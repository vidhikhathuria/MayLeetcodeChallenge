# Problem Link: https://leetcode.com/problems/valid-perfect-square/
class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        n = 1
        odd = 1
        while n < num:
            odd += 2
            n += odd

        if n == num:
            return True
        else:
            return False

