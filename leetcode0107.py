# Problem Link: https://leetcode.com/problems/cousins-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def heightOfNode(root, x, h):
            if root == None:
                return 0
            if root.val == x:
                return h
            # if root.left != None or root.right != None:
            return max(heightOfNode(root.left, x, h + 1), heightOfNode(root.right, x, h + 1))

        def checkParent(root, x):
            print(root, x)
            if root == None:
                return 0
            if (root.left != None and root.left.val == x) or (root.right != None and root.right.val == x):
                return root.val
            p = 0
            if root.left != None:
                p = checkParent(root.left, x)
            if p == 0 and root.right != None:
                p = checkParent(root.right, x)
            return p

        heightx = heightOfNode(root, x, 0)
        heighty = heightOfNode(root, y, 0)
        if heightx == heighty:
            px = checkParent(root, x)
            py = checkParent(root, y)
            print(px, py)
            if px != py:
                return True
            else:
                return False
        else:
            return False



