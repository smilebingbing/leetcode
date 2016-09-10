# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        p=ListNode(0)
        fast=head
        slow=head
        while fast.next!=None and fast.next.next!=None:
            fast=fast.next.next
            slow=slow.next
        fast=slow
        slow=slow.next
        fast.next=None
        L1=self.sortList(head)
        L2=self.sortList(slow)
        return self.mergeTwoLists(L1,L2)
    def mergeTwoLists(self,L1,L2):
        if L1==None:
            return L2
        if L2==None:
            return L1
        p=ListNode(0)
        tmp=p
        while L1 and L2:
            if L1.val>=L2.val:
                tmp.next=L2
                L2=L2.next
            else:
                tmp.next=L1
                L1=L1.next
            tmp=tmp.next
        if L1==None:
            tmp.next=L2
        else:
            tmp.next=L1
        return p.next

'''
accept
'''
