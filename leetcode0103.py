# Problem Link : https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = set(ransomNote)
        for i in m:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True