from typing import List
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        expected = list(range(1,n)) + [n - 1]

        return nums == expected