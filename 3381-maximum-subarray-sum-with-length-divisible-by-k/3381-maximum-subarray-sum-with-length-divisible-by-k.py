class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        INF = 10 ** 20
        min_pref = [INF] * k
        min_pref[0] = 0

        prefix = 0
        best = -INF

        for i,x in enumerate(nums,1):
            prefix += x
            r = i % k
            best = max(best, prefix - min_pref[r])
            min_pref[r] = min(min_pref[r], prefix)
        return best
