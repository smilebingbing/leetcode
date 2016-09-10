# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        if root==None:
            return res
        thislevel=[root]
        need_reverse=False
        while thislevel:
            level_res=[]
            next_level=[]
            for tmp in thislevel:
                level_res.append(tmp.val)
                if tmp.left:
                    next_level.append(tmp.left)
                if tmp.right:
                    next_level.append(tmp.right)
            if need_reverse:
                level_res.reverse()
                need_reverse=False
            else:
                need_reverse=True
            res.append(level_res)
            thislevel=next_level
        return res

        

