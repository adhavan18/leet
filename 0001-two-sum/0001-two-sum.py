class Solution:
    def twoSum(self, nums: arr, target: int) -> int:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]