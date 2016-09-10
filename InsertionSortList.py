# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p=ListNode(0)
        p.next=head
        cur=head
        while cur.next:
            if cur.next.val<cur.val:
                pre=p
                while pre.next.val<cur.next.val:
                    pre=pre.next
                tmp=cur.next
                cur.next=tmp.next
                tmp.next=pre.next
                pre.next=tmp
            else:
                cur=cur.next
        return p.next

'''
accept
'''