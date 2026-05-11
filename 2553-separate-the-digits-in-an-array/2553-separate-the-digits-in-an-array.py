class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            s = str(nums)
            for ch in s:
                result.append(int(ch))
        return result
