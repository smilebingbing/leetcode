# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:return None
        self.preorder,self.inorder=preorder,inorder
        self.itable={v:i for i,v in enumerate (inorder)}
        return self.dfs(0,0,len(preorder))
    def dfs(self,preLeft,inLeft,Len):
        if Len<=0:
            return None
        root=TreeNode(self.preorder[preLeft])
        rootPos=self.itable[self.preorder[preLeft]]
        lsize=rootPos-inLeft
        rsize=Len-lsize-1
        root.left=self.dfs(preLeft+1,inLeft,rootPos-inLeft)
        root.right=self.dfs(preLeft+1+lsize,rootPos+1,Len-1-(rootPos-inLeft))
        return root
'''
accept
'''

