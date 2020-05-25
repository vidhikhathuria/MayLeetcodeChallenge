# Problem Link : https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
     # I accidentally wrote code for returning an array, using stack , then realised im supposed to return treenode so rewrote code.

     #   	import math
     #    ans = [None] * ((2 ** math.ceil(math.sqrt(len(preorder)))) - 1)
     #    stack = []
     #    indices = []
     #    parent = 0
     #    child = 0
     #    for i in range(len(preorder)):
     #        if len(stack) == 0 or stack[-1] >= preorder[i]:
     #            if len(stack):
     #                child = indices[-1] * 2 + 1
     #        else:
     #            while len(stack):
     #                if stack[-1] >= preorder[i]:
     #                    break
     #                var = stack.pop()
     #                idx = indices.pop()
     #            child = idx * 2 + 2
     #        stack.append(preorder[i])
     #        indices.append(child)
     #        ans[child] = preorder[i]
     #    print(ans) 
        
        def bst(root, var):
            if root == None:
                root = TreeNode(val = var)
            if root.val > var:
                if root.left is None: 
                    root.left = TreeNode(val = var) 
                else: 
                    bst(root.left, var) 
            else:
                if root.right is None: 
                    root.right = TreeNode(val = var) 
                else: 
                    bst(root.right, var) 
            
            
        root = TreeNode(val = preorder[0])
        for i in range(1, len(preorder)):
            bst(root, preorder[i])
        
        return root
        
        
