class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_count: int, close_count: int, current_str: str):
            # Base case: if the current string reaches length 2 * n, we found a valid combination
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            # Can add an opening bracket if we haven't reached 'n' opening brackets yet
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")
            
            # Can add a closing bracket if there are more opening brackets than closing ones
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")

        backtrack(0, 0, "")
        return res