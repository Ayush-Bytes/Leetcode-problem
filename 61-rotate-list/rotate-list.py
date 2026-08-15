# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge cases: Empty list, single node, ya no rotation
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: List ki length (length) find karein aur tail reach karein
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Unnecessary rotations ko eliminate karein
        k = k % length
        if k == 0:
            return head
        
        # Step 3: List ko circular banana (tail -> head)
        tail.next = head
        
        # Step 4: Naye tail tak traversal (length - k - 1 steps)
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        # Step 5: Naya head set karein aur ring ko break karein
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head