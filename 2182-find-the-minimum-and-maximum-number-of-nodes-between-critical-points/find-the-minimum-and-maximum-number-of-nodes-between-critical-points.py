# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        index = 1  # 0-indexed offset, head.next is at index 1
        
        first_cp = -1
        last_cp = -1
        min_dist = float('inf')
        
        while curr and curr.next:
            # Check if current node is a critical point (local maxima or minima)
            is_maxima = prev.val < curr.val and curr.val > curr.next.val
            is_minima = prev.val > curr.val and curr.val < curr.next.val
            
            if is_maxima or is_minima:
                if first_cp == -1:
                    first_cp = index
                else:
                    min_dist = min(min_dist, index - last_cp)
                
                last_cp = index
            
            prev = curr
            curr = curr.next
            index += 1
            
        # If less than 2 critical points were found
        if first_cp == -1 or first_cp == last_cp:
            return [-1, -1]
            
        max_dist = last_cp - first_cp
        return [min_dist, max_dist]