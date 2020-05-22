# Problem Link: https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(list)
        for i in set(list(s)):
            st = ''
            n = s.count(i)
            for j in range(n):
                st += i
            d[n].append(st)
        st = ''
        for i in sorted(d.keys(), reverse=True):
            for j in d[i]:
                st += j
        return st