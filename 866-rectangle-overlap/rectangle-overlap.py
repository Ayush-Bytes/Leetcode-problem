class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Unpack coordinates
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        
        # 1. rec1 is to the left of rec2
        # 3. rec1 is below rec2
        is_not_overlapping = (x2 <= x3) or (x1 >= x4) or (y2 <= y3) or (y1 >= y4)
        
        return not is_not_overlapping