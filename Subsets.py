class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        for i in sorted(nums):
            res+=[item+[i] for item in res]
        return res