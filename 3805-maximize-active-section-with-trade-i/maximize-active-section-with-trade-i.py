class Solution:

  def maxActiveSectionsAfterTrade(self, s: str) -> int:
    # 1. Total ones in the original string s
    initial_ones = s.count('1')

    # 2. Augment s with '1' at both ends
    t = '1' + s + '1'

    # 3. Group string into consecutive segments (character, length)
    segments = []
    i = 0
    n = len(t)
    while i < n:
      j = i
      while j < n and t[j] == t[i]:
        j += 1
      segments.append((t[i], j - i))
      i = j

    # 4. Find the maximum gain (delta) by checking '1' segments surrounded by '0's
    max_delta = 0
    for k in range(1, len(segments) - 1):
      if (
          segments[k][0] == '1'
          and segments[k - 1][0] == '0'
          and segments[k + 1][0] == '0'
      ):
        delta = segments[k - 1][1] + segments[k + 1][1]
        max_delta = max(max_delta, delta)

    # 5. Result is initial ones plus maximum delta achieved
    return initial_ones + max_delta