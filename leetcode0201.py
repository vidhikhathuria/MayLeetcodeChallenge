# Problem Link: https://leetcode.com/problems/check-if-it-is-a-straight-line/
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        else:
            try:
                m = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
                b = coordinates[0][1] - (coordinates[0][0] * m)
                for i in coordinates[2:]:
                    a = i[0] * m + b
                    if i[1] != int(a):
                        return False
                return True
            except ZeroDivisionError:
                for i in coordinates[2:]:
                    if i[0] != coordinates[0][0]:
                        return False
                return True