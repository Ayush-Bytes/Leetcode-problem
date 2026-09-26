class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = {k: v for k, v in knowledge}
        
        res = []
        inside_bracket = False
        key = []
        
        for char in s:
            if char == '(':
                inside_bracket = True
                key = []
            elif char == ')':
                k_str = "".join(key)
                res.append(mapping.get(k_str, "?"))
                inside_bracket = False
            elif inside_bracket:
                key.append(char)
            else:
                res.append(char)
                
        return "".join(res)