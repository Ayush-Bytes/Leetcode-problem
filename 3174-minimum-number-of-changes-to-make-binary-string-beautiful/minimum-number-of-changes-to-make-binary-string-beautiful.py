class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        # Step-by-step 2 length ke consecutive blocks ko check karenge
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                changes += 1
        return changes