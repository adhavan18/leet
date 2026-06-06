from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            leftSum = 0
            rightSum = 0

            for j in range(len(nums)):
                if j < i:
                    leftSum += nums[j]
                elif j > i:
                    rightSum += nums[j]

            answer.append(abs(leftSum - rightSum))

        return answer