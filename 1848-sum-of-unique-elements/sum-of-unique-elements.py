class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count == 1:
                ans += nums[i]
        return ans
                