# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        if root==None:
            return res
        level=[root]
        while len(level)>0:
            numberlevel=[]
            nextlevel=[]
            for tmp in level:
                numberlevel.append(tmp.val)
                if tmp.left!=None:
                    nextlevel.append(tmp.left)
                if tmp.right!=None:
                    nextlevel.append(tmp.right)
            res.append(numberlevel)
            level=nextlevel
        return res