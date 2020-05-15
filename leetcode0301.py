# Problem Link: https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, a: List[int]) -> int:
        def kadane(a): 
            n = len(a) 
            max_so_far = 0
            max_ending_here = 0
            for i in range(0, n): 
                max_ending_here = max_ending_here + a[i] 
                if (max_ending_here < 0): 
                    max_ending_here = 0
                if (max_so_far < max_ending_here): 
                    max_so_far = max_ending_here 
            return max_so_far 

        n = len(a) 
        max_kadane = kadane(a)         
        max_wrap = 0
        flag = 0
        arr = [0] * n
        for i in range(0,n): 
            if a[i] > 0:
                flag = 1
            max_wrap += a[i] 
            arr[i] = -a[i]
        if flag == 0:
            return max(a)
        max_wrap = max_wrap + kadane(arr) 
        if max_wrap > max_kadane: 
            return max_wrap 
        else: 
            return max_kadane 
        