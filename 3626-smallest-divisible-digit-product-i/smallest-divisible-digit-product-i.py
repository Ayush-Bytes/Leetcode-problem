class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def get_digit_product(num: int) -> int:
            product = 1
            for digit in str(num):
                product *= int(digit)
            return product

        while True:
            if get_digit_product(n) % t == 0:
                return n
            n += 1