# Problem Link : https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, arr: List[int]) -> int:
        n = len(arr)
        hash_map = dict()
        curr_sum = 0
        max_len = 0
        ending_index = -1
        for i in range (0, n): 
            curr_sum += arr[i] if arr[i] else -1
            # print(i, arr[i],curr_sum, hash_map, max_len)
            if (curr_sum == 0): 
                max_len = i + 1
                ending_index = i 
            if curr_sum in hash_map: 
                if max_len < i - hash_map[curr_sum]: 
                    max_len = i - hash_map[curr_sum] 
                    ending_index = i 
            else: 
                hash_map[curr_sum] = i 
        return max_len