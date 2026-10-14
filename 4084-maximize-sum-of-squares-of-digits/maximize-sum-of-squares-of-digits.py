class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > num * 9:
            return ""
        
        res = []
        for i in range(num):
            rem_slots = num - 1 - i
            # Left se largest number banane ke liye greedy approach:
            # Current digit ko utna bada rakho jitna possible ho, 
            # par baaki ke slots ke liye itna sum zaroor bache jo manage ho sake.
            current_digit = min(9, sum - rem_slots * 0) 
            
            # Lekin agar sum kam pad raha hai baaki slots ke liye, toh current digit ko adjust karo:
            # Baaki slots maximum (rem_slots * 9) le sakte hain, toh current ko at least (sum - rem_slots * 9) dena padega.
            min_needed = max(0, sum - rem_slots * 9)
            
            # Aur maximum kya de sakte hain?
            max_allowed = min(9, sum)
            
            # Humein largest number chahiye, isliye hum greedy tarike se max se start karenge 
            # ya loop laga kar check kar lenge:
            for d in range(max_allowed, min_needed - 1, -1):
                res.append(str(d))
                sum -= d
                break
                
        return "".join(res)