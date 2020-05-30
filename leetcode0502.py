# Problem Link : https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from collections import defaultdict
        d = defaultdict(list)
        for i in points:
            d[(i[0]) ** 2 + (i[1]) ** 2].append(i)
        arr = []
        n = sorted(d.keys())
        for i in n:
            for j in d[i]:
                arr.append(j)
                k -= 1
                if k == 0:
                    return arr
        return arr