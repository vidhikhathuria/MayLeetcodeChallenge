# Problem Link : https://leetcode.com/problems/kth-smallest-element-in-a-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        li = []
        curr = root
        stack = []
        while len(li) != k:
            if curr is not None: 
                stack.append(curr) 
                curr = curr.left  
            elif(stack): 
                curr = stack.pop() 
                li.append(curr.val)
                curr = curr.right  
            else: 
                break
        if len(li):
            return li[-1]
        else:
            return None