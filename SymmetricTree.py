# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.isSameTree(root.left,root.right)
        return True
    def isSameTree(self,p,q):
        if p==None and q==None:
            return True
        if p and q and p.val==q.val:
            return self.isSameTree(p.right,q.left) and self.isSameTree(p.left,q.right)
        return False