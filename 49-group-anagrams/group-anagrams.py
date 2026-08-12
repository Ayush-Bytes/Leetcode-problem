from collections import defaultdict
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            # Sort the characters in string s to use as a key
            sorted_str = "".join(sorted(s))
            anagram_map[sorted_str].append(s)

        # Return all grouped anagrams as a list of lists
        return list(anagram_map.values())