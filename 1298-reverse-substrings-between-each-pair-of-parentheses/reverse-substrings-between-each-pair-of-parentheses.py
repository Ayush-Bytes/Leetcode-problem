class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                current_chars = []
                while stack and stack[-1] != '(':
                    current_chars.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()  # Remove '('
                for c in current_chars:
                    stack.append(c)
            else:
                stack.append(char)
        return "".join(stack)