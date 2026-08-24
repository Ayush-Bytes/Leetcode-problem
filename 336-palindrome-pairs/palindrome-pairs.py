from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_to_idx = {word: i for i, word in enumerate(words)}
        res = []

        for i, word in enumerate(words):
            n = len(word)
            
            for k in range(n + 1):
                prefix = word[:k]
                suffix = word[k:]

                if prefix == prefix[::-1]:
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_to_idx and word_to_idx[rev_suffix] != i:
                        res.append([word_to_idx[rev_suffix], i])

                # Case 2: If suffix is palindrome, look for reverse(prefix) after word
                # len(suffix) != 0 handles the overlapping empty suffix edge case
                if len(suffix) != 0 and suffix == suffix[::-1]:
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_to_idx and word_to_idx[rev_prefix] != i:
                        res.append([i, word_to_idx[rev_prefix]])

        return res