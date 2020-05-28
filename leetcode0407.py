# Problem Link : https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, num: int) -> List[int]:
        import math
        ans = [0, 1, 1, 2]
        li = [1, 2]
        if num <= 3:
            for i in range(0, 3 - num):
                ans.pop()
            return ans
        sq = math.ceil(math.sqrt(num))
        for i in range(1, sq):
            if len(ans) > num:
                break
            li2 = li.copy()
            li3 = li[int(len(li) / 2):].copy()
            li4 = [(i + 1) for i in li3]
            li = []
            li.extend(li2)
            li.extend(li3)
            li.extend(li4)
            ans.extend(li)
            # print(li,li2, li3, li4)
        
            
        return ans[:num + 1]