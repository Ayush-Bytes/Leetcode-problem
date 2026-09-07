class Solution:

  def distinctSubseqII(self, s: str) -> int:
    MOD = 10**9 + 7
    # last_added[c] stores the count of distinct subsequences ending with character 'c'
    last_added = [0] * 26

    for char in s:
      idx = ord(char) - ord('a')
      # New subsequences created by appending current character = (sum of all previous distinct subsequences + 1)
      new_count = (sum(last_added) + 1) % MOD
      last_added[idx] = new_count

    return sum(last_added) % MOD