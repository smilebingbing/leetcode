class Solution(object):
    def levelOrderBottom(self,root):
        res=[]
        if root==None:
            return res
        levelTo=[root]
        while len(levelTo)>0:
            numlevel=[]
            nextlevel=[]
            for tmp in levelTo:
                numlevel.append(tmp.val)
                if tmp.left!=None:
                    nextlevel.append(tmp.left)
                if tmp.right!=None:
                    nextlevel.append(tmp.right)
            res.append(numlevel)
            levelTo=nextlevel
        return res.reverse()