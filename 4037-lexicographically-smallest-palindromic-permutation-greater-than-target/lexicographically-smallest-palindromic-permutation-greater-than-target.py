from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        odd_count = sum(1 for c in cnt if cnt[c] % 2 != 0)
        if odd_count > 1:
            return ""
        
        half_cnt = {c: count // 2 for c, count in cnt.items() if count // 2 > 0}
        mid_char = next((c for c in cnt if cnt[c] % 2 != 0), None)
        
        k = n // 2
        
        
        for i in range(k, -1, -1):
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
            
            if i == k:
                if n % 2 != 0:
                    if mid_char and mid_char > target[k]:
                        first_half = target[:k]
                        return first_half + mid_char + first_half[::-1]
                first_half = target[:k]
                full_palin = first_half + (mid_char if mid_char else "") + first_half[::-1]
                if full_palin > target:
                    return full_palin
                continue

            target_char = target[i]
            
            sorted_chars = sorted(cur_half_cnt.keys())
            for ch in sorted_chars:
                if ch > target_char and cur_half_cnt[ch] > 0:
                    temp_cnt = cur_half_cnt.copy()
                    temp_cnt[ch] -= 1
                    
                    rem_half = []
                    for c in sorted(temp_cnt.keys()):
                        rem_half.extend([c] * temp_cnt[c])
                    
                    first_half = target[:i] + ch + "".join(rem_half)
                    
                    mid = mid_char if mid_char else ""
                    
                    res = first_half + mid + first_half[::-1]
                    
                    if res > target:
                        return res

        return ""