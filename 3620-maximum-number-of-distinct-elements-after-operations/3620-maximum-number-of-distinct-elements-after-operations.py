class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        last = -10**18  # track last used number
        for x in nums:
            # pick the smallest possible number >= last + 1 within [x - k, x + k]
            val = max(x - k, last + 1)
            if val <= x + k:
                res += 1
                last = val
        return res