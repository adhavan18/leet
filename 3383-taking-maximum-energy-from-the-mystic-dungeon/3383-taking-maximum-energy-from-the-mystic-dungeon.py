# class Solution:
#     def maximumEnergy(self, energy: list[int], k: int) -> int:
#         max_total = -999999999
#
#         for start in range(len(energy)):
#             total = 0
#             i = start
#             while i < len(energy):
#                 total += energy[i]
#                 i +=    # <-- you'll need to fill this with k
#             max_total = max(max_total, total)
#
#         return max_total

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        result = float('-inf')
        for i in range(n - 1, -1, -1):
            dp[i] = energy[i] + (dp[i + k] if i + k < n else 0)
            result = max(result, dp[i])
        return result
