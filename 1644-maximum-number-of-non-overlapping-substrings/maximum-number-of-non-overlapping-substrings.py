class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        # Find first and last occurrence for every character
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
            
        intervals = []
        
        # Check every unique character in the string
        for c in set(s):
            i = first[c]
            right = last[c]
            valid = True
            j = i
            while j <= right:
                # If any character inside this range starts before our start index 'i',
                # then this substring cannot be independent.
                if first[s[j]] < i:
                    valid = False
                    break
                right = max(right, last[s[j]])
                j += 1
            
            if valid:
                intervals.append((i, right))
        
        # Greedy interval scheduling: sort by end time, then by length
        intervals.sort(key=lambda x: (x[1], x[1] - x[0]))
        
        result = []
        prev_end = -1
        for start, end in intervals:
            # If this interval doesn't overlap with the previous chosen one
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end
                
        return result