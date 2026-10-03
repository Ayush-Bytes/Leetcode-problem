class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base case: when the string length reaches 2 * n, we have a valid combination
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # We can add an opening parenthesis if we haven't used all n of them
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # We can add a closing parenthesis if there are unclosed opening parentheses
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return result