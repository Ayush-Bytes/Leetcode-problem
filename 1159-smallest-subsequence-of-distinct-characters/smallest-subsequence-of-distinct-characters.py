class Solution:
    def smallestSubsequence(self, s: str) -> str:
       
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()  
        for i, char in enumerate(s):

            if char in seen:
                continue
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)

            stack.append(char)
            seen.add(char)
            
        return "".join(stack)