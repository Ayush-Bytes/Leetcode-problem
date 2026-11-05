from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            # Find the insertion index of x in arr2
            idx = bisect_left(arr2, x)
            
            # Check the closest elements in arr2 (if they exist)
            valid = True
            if idx < len(arr2) and abs(arr2[idx] - x) <= d:
                valid = False
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                valid = False
                
            if valid:
                distance_value += 1
                
        return distance_value