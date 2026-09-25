class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        res, cur = set(), set([""])

        for char in expression:
            if char.isalpha():
                cur = {c + char for c in cur}
            elif char == '{':
                stack.append(res)
                stack.append(cur)
                res, cur = set(), set([""])
            elif char == ',':
                res.update(cur)
                cur = set([""])
            elif char == '}':
                # Close current scope
                res.update(cur)
                prev_cur = stack.pop()
                prev_res = stack.pop()
                
                cur = {p + r for p in prev_cur for r in res}
                res = prev_res

        res.update(cur)
        return sorted(list(res))