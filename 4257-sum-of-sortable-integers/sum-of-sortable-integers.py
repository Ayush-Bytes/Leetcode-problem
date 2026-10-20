class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Prefix maximum
        pref_max = [0] * (n + 1)

        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        # Step 2: Suffix minimum
        suff_min = [float('inf')] * (n + 1)

        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        # Step 3: Count adjacent decreasing pairs
        pref_drop = [0] * n

        for i in range(1, n):
            pref_drop[i] = (
                pref_drop[i - 1] + (nums[i - 1] > nums[i])
            )

        # Step 4: Check whether k is sortable
        def check(k):
            for start in range(0, n, k):
                end = start + k - 1

                # Count decreasing pairs inside the block
                drops = pref_drop[end] - pref_drop[start]

                # Check circular boundary
                if nums[end] > nums[start]:
                    drops += 1

                # Check whether this block can be sorted
                if drops > 1:
                    return False

                # Check ordering between blocks
                if pref_max[start] > suff_min[start]:
                    return False

            return True

        # Step 5: Find all divisors of n
        ans = 0
        k = 1

        while k <= n // k:
            if n % k == 0:

                if check(k):
                    ans += k

                other = n // k

                if other != k and check(other):
                    ans += other

            k += 1

        return ans