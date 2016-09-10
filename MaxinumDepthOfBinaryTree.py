# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        if root.left==None and root.right!=None:
            return self.maxDepth(root.right)+1
        if root.left!=None and root.right==None:
            return self.maxDepth(root.left)+1
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1 