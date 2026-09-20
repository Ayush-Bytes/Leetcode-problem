class Solution:

  def reverseDegree(self, s: str) -> int:
    total_degree = 0
    for i, char in enumerate(s):
      string_index = i + 1
      reversed_alphabet_index = 26 - (ord(char) - ord('a'))

      total_degree += reversed_alphabet_index * string_index

    return total_degree