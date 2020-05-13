# Problem Link: https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(0, len(nums), 2):
            if (i + 1 < len(nums) and nums[i] != nums[i + 1]) or (i + 1 == len(nums)):
                return nums[i]
