# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        current = head
        while current:
            length+=1
            current=current.next

        position=0
        current = head
        if n == 1 and length == 1:
            self.head=None
            return None
        if length-n == 0:
                head=head.next
                return head
        while current:
                  
            if position == length-n-1:
                current.next=current.next.next
                return  head
            position+=1
            current=current.next
        