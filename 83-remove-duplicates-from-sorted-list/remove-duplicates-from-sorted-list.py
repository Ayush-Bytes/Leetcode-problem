# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Duplicate mila, to next node ko skip (delete) perform karo
                curr.next = curr.next.next
            else:
                # Unique value milli, aage bado
                curr = curr.next
                
        return head