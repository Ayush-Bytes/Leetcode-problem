from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        # 1. Check if valid palindromic permutation is possible
        odd_count = sum(1 for c in cnt if cnt[c] % 2 != 0)
        if odd_count > 1:
            return ""
        
        # Store available character pairs for the first half
        half_cnt = {c: count // 2 for c, count in cnt.items() if count // 2 > 0}
        mid_char = next((c for c in cnt if cnt[c] % 2 != 0), None)
        
        k = n // 2
        
        # Try to find the longest common prefix match with `target` up to index i-1,
        # and at index i, put a character > target[i].
        
        # We iterate from longest possible prefix (k) down to 0
        for i in range(k, -1, -1):
            # Check if target[:i] can be formed by half_cnt
            cur_half_cnt = half_cnt.copy()
            possible = True
            
            for j in range(i):
                ch = target[j]
                if cur_half_cnt.get(ch, 0) > 0:
                    cur_half_cnt[ch] -= 1
                else:
                    possible = False
                    break
            
            if not possible:
                continue
            
            # Case 1: Match first k characters exactly, and check middle character (if n is odd)
            if i == k:
                if n % 2 != 0:
                    # Target's mid char vs mid_char
                    if mid_char and mid_char > target[k]:
                        # Form exact prefix target[:k] + mid_char + reversed(target[:k])
                        first_half = target[:k]
                        return first_half + mid_char + first_half[::-1]
                # If even length or mid_char doesn't make it strictly greater, check mirror condition
                first_half = target[:k]
                full_palin = first_half + (mid_char if mid_char else "") + first_half[::-1]
                if full_palin > target:
                    return full_palin
                continue

            # Case 2: At index i < k, pick a character > target[i]
            target_char = target[i]
            
            # Try available characters strictly greater than target[i]
            sorted_chars = sorted(cur_half_cnt.keys())
            for ch in sorted_chars:
                if ch > target_char and cur_half_cnt[ch] > 0:
                    # Place 'ch' at index i
                    temp_cnt = cur_half_cnt.copy()
                    temp_cnt[ch] -= 1
                    
                    # Construct remaining first half with smallest available characters
                    rem_half = []
                    for c in sorted(temp_cnt.keys()):
                        rem_half.extend([c] * temp_cnt[c])
                    
                    first_half = target[:i] + ch + "".join(rem_half)
                    
                    # Construct middle character if n is odd
                    mid = mid_char if mid_char else ""
                    
                    # Full palindrome
                    res = first_half + mid + first_half[::-1]
                    
                    if res > target:
                        return res

        return ""