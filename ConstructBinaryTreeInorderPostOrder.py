# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None
        if len(inorder)==1:
            return TreeNode(inorder[0])
        root=TreeNode(postorder[len(postorder)-1])
        index=inorder.index(postorder[len(postorder)-1])
        root.left=self.buildTree(inorder[0:index],postorder[0:index])
        root.right=self.buildTree(inorder[index+1:len(inorder)],postorder[index:len(postorder)-1])
        return root
'''
'''
class Solution(object):
    def buildTree(self,inorder,postorder):
        if not inorder:return None
        root=TreeNode(postorder[-1])
        index=inorder.index(postorder[-1])
        root.left=self.buildTree(inorder[:index],postorder[:index])
        root.right=self.buildTree(inorder[index+1:],postorder[index:-1])
        return root

        Memory limited exceed
'''
class Solution(object):
    def buildTree(self,inorder,postorder):
        if not inorder:return None
        self.inorder,self.postorder=inorder,postorder
        return self.dfs(0,0,len(inorder))

    def dfs(self,inLeft,postLeft,Len):
        if Len<=0:
            return None
        root=TreeNode(self.postorder[postLeft+Len-1])
        rootPos=self.inorder.index(self.postorder[postLeft+Len-1])
        root.left=self.dfs(inLeft,postLeft,rootPos-inLeft)
        root.right=self.dfs(rootPos+1,postLeft+rootPos-inLeft,Len-1-(rootPos-inLeft))
        return root
'''
memory limited exceed 列表切片是产生新的列表，以前的列表没有释放，所以会造成内存溢出，
accept  用实例变量
'''