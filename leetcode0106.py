# Problem Link: https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = set(nums)
        l = len(nums)
        for i in n:
            if nums.count(i) > l / 2:
                return i
