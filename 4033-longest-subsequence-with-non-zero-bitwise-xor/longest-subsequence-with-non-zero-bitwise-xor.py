class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        all_zero = True
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                all_zero = False
                
        # Agar saare elements 0 hain, toh XOR hamesha 0 hi rahega
        if all_zero:
            return 0
            
        # Agar poore array ka XOR non-zero hai, toh pure array ko subsequence le sakte hain
        if total_xor != 0:
            return len(nums)
            
        # Agar total XOR 0 hai par kam se kam ek element non-zero hai, 
        # toh kisi ek element ko hata kar non-zero XOR mil jayega
        return len(nums) - 1