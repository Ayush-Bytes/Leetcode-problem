class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0
        cmax = 0
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            else:  # char == '*'
                cmin -= 1
                cmax += 1
                
            if cmax < 0:
                return False
            cmin = max(0, cmin)
            
        return cmin == 0