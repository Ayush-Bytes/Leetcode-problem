class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        res, cur = set(), set([""])

        for char in expression:
            if char.isalpha():
                # Concatenation: Append character to all current combinations
                cur = {c + char for c in cur}
            elif char == '{':
                # Save current state on stack
                stack.append(res)
                stack.append(cur)
                res, cur = set(), set([""])
            elif char == ',':
                # Union operation: Combine current with previous results
                res.update(cur)
                cur = set([""])
            elif char == '}':
                # Close current scope
                res.update(cur)
                prev_cur = stack.pop()
                prev_res = stack.pop()
                
                # Multiply previous state with expanded inside scope
                cur = {p + r for p in prev_cur for r in res}
                res = prev_res

        res.update(cur)
        return sorted(list(res))