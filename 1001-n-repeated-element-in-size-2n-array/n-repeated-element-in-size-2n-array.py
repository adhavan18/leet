class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                
            if count[num] == len(nums) // 2:
                return num