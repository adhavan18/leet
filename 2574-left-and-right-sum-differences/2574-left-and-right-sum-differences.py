from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            leftSum = sum(nums[:i])
            rightSum = sum(nums[i + 1:])
            answer.append(abs(leftSum - rightSum))

        return answer