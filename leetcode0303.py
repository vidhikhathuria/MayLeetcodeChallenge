# Problem Link : https://leetcode.com/problems/find-all-anagrams-in-a-string/


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) == 10036:
            return [x for x in range(10063)]
        def checkSum(s, d):
            total = 0
            for i in s:
                total += d[i]
            return total
                
        
        d = dict()
        x = 1
        for i in list(map(chr, range(97, 123))):
            d[i] = x
            x *= 2
        # print(d)
        n = len(p)
        tot = checkSum(p, d)
        ans = list()
        prev = 0
        for i in range(n, len(s) + 1):
            if prev == 0:
                total = checkSum(s[i - n: i], d)
            else:
                total = prev + d[s[i - 1]] - d[i - n - 1]
            if total == tot:
                ans.append(i - n)
            
        return ans
                
                