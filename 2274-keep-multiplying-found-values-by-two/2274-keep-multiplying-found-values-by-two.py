class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        #first we have to check whether original is there in nums
        while original in nums:
            original = original * 2  #original *= 2
        return original

        