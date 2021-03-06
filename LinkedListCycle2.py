# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1=p2=head
        while p1 and p1.next:
            p1=p1.next.next
            p2=p2.next
            if p1==p2:
                break
        else:
            return None
        while head!=p1:
            p1=p1.next
            head=head.next
        return head
     