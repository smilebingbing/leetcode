# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        p=ListNode(0)
        tmp=p
        while l1 and l2:
            if l1.val>=l2.val:
                tmp.next=l2
                l2=l2.next
                tmp=tmp.next
            else:
                tmp.next=l1
                l1=l1.next
                tmp=tmp.next
        if l1==None:
            tmp.next=l2
        else:
            tmp.next=l1
        return p.next