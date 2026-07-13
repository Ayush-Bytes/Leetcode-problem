class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        
        for length in range(2, 10):
            for start in range(10 - length):

                num = int(digits[start : start + length])

                if low <= num <= high:
                    result.append(num)
                elif num > high:

                    break
                    
        return result