class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute divisors for each length
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        
        # cost[i][j] = min changes to make s[i...j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                sub = s[i:j+1]
                
                min_changes = float('inf')
                for d in divisors[length]:
                    current_changes = 0
                    for start in range(d):
                        group = sub[start::d]
                        m = len(group)
                        for idx in range(m // 2):
                            if group[idx] != group[m - 1 - idx]:
                                current_changes += 1
                    min_changes = min(min_changes, current_changes)
                cost[i][j] = min_changes
                
        # DP table to find minimum changes for k partitions
        dp = {}
        
        def solve(i, rem):
            if rem == 1:
                if i < n:
                    return cost[i][n - 1]
                return float('inf')
            
            if i >= n:
                return float('inf')
                
            if (i, rem) in dp:
                return dp[(i, rem)]
            
            res = float('inf')
            # Har remaining part ki minimum length 2 honi chahiye
            for j in range(i, n - 2 * (rem - 1)):
                c = cost[i][j]
                if c != float('inf'):
                    res = min(res, c + solve(j + 1, rem - 1))
                
            dp[(i, rem)] = res
            return res

        ans = solve(0, k)
        return int(ans) if ans != float('inf') else 0