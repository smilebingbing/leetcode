# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        def dfs(root,cursum,valuelist):
            if root.left==None and root.right==None:
                if sum==cursum:
                    res.append(valuelist)
            if root.left:
                return self.dfs(root.left,cursum+root.left.val,valuelist+[root.left.val])
            if root.right:
                return self.dfs(root.right,cursum+root.right.val,valuelist+[root.right.val]
        
        if root==None: return []
        res=[]
        self.dfs(root,root.val,[root.val])
        return res

'''
not accept
'''