from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Key: row_number, Value: bitmask of reserved seats from column 2 to 9
        seats = defaultdict(int)
        
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                # col - 2 se 0-indexed bit representation milta hai (bit 0 to bit 7)
                seats[row] |= (1 << (col - 2))
        
        # Jin rows me koi reservation nahi hai, unme 2 groups baith sakte hain
        max_groups = (n - len(seats)) * 2
        
        # Bitmasks for checking availability (4 contiguous seats must be 0)
        # 15 = 0b00001111 (Seats 2,3,4,5)
        # 240 = 0b11110000 (Seats 6,7,8,9)
        # 60 = 0b00111100 (Seats 4,5,6,7)
        
        for reserved_mask in seats.values():
            allocated = False
            
            # Check left side (seats 2,3,4,5)
            if not (reserved_mask & 15):
                max_groups += 1
                allocated = True
                
            # Check right side (seats 6,7,8,9)
            if not (reserved_mask & 240):
                max_groups += 1
                allocated = True
                
            # Agar left aur right me se kisi me jagah nahi mili, toh middle check karo
            if not allocated and not (reserved_mask & 60):
                max_groups += 1
                
        return max_groups