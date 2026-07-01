# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s= ListNode(0,head)
        fast = s
        slow = s
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast=fast.next
            slow = slow.next

        slow.next=slow.next.next
        return s.next