# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list=[]
        self.iterative_preorder(self,list)
        return list
    def recursive_preorder(self,root,list):
        if root:
            list.append(root.val)
            self.preorder(root.left,list)
            self.preorder(root.right,list)
    def iterative_preorder(self,root,list):
        stack=[]
        while root or stack:
            if root:
                list.append(root.val)
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                root=root.right
        return list 



"""
class Solution(object):
    def preorderTraversal(self,root):
        if root is None:
            return []
        stack=[root]
        preorder=[]
        while stack:
            node=stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder
"""