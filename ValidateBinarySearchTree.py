# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        infinity=10**10
        return self.Validate(root,-infinity,infinity)
    def Validate(self,root,min,max):
        if root==None:
            return True
        if root.val<=min or root.val>=max:
            return False
        return self.Validate(root.left,min,root.val) and self.Validate(root.right,root.val,max)
