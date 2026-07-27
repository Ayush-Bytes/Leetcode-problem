class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0
        n1, n2 = len(word1), len(word2)
        
        while i < n1 and j < n2:
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
            
        if i < n1:
            result.append(word1[i:])
            
        if j < n2:
            result.append(word2[j:])
            
        return "".join(result)