class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        left = {}
        right = {}

        for x in nums:
            right[x] = right.get(x, 0) + 1

        ans = 0

        for x in nums:
            right[x] -= 1
            need = x * 2
            ans = (ans + left.get(need, 0) * right.get(need, 0)) % MOD
            left[x] = left.get(x, 0) + 1

        return ans