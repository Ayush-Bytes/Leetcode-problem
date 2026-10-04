class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        
        for i, char in enumerate(s):
            if char == '(':
                left_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else:  # char == ')'
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
                    
        # Match remaining '(' with '*' that appear after them
        while left_stack and star_stack:
            if left_stack[-1] < star_stack[-1]:
                left_stack.pop()
                star_stack.pop()
            else:
                break
                
        return len(left_stack) == 0