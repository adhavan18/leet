class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            r = x % 3
            if r == 0:
                continue
            if r == 1:
                count += 1
            else:
                count += 1

        return count
