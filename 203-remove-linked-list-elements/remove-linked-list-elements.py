# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        current= head
        while current and current.next:
            prev=current
            if current.next.val == val:
                prev.next = prev.next.next
            else:
                current=current.next

        return head