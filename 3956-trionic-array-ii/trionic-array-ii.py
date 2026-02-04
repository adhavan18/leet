class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        
        import math

        dp0 = nums[0]
        dp1 = dp2 = dp3 = -math.inf

        
        ans = -math.inf

        for i in range(1, len(nums)):
            x = nums[i]

            new_dp0 = x
            new_dp1 = new_dp2 = new_dp3 = -math.inf

            if x > nums[i - 1]:
                new_dp1 = max(dp1, dp0) + x
                new_dp3 = max(dp3, dp2) + x

            if x < nums[i - 1]:
                new_dp2 = max(dp2, dp1) + x

            dp0, dp1, dp2, dp3 = new_dp0, new_dp1, new_dp2, new_dp3
            ans = max(ans, dp3)

        return ans
