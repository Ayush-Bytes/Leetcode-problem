class Solution:

  def minOperations(self, s: str) -> int:
    # Case 1: Already sorted
    if s == "".join(sorted(s)):
      return 0

    n = len(s)
    # Case 2: Length 2 cannot be sorted if not already sorted
    if n == 2:
      return -1

    min_char = min(s)
    max_char = max(s)

    # Case 3: Minimum is at the start (excluding the whole string) or Maximum is at the end
    if s[0] == min_char or s[-1] == max_char:
      return 1

    # Check if we can do it in 2 or 3 operations based on boundaries
    has_min_in_prefix = any(s[i] == min_char for i in range(n - 1))
    has_max_in_suffix = any(s[i] == max_char for i in range(1, n))

    if not has_min_in_prefix and not has_max_in_suffix:
      return 3

    return 2