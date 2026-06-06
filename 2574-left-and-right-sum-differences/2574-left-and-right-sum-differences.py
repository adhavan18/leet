from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Efficient O(n) Solution
        totalSum = sum(nums)
        leftSum = 0
        answer = []

        for num in nums:
            rightSum = totalSum - leftSum - num
            answer.append(abs(leftSum - rightSum))
            leftSum += num

        return answer


        # --------------------------------------------------
        # Brute Force O(n²) using slicing
        # --------------------------------------------------
        #
        # answer = []
        #
        # for i in range(len(nums)):
        #     leftSum = sum(nums[:i])
        #     rightSum = sum(nums[i + 1:])
        #     answer.append(abs(leftSum - rightSum))
        #
        # return answer


        # --------------------------------------------------
        # Brute Force O(n²) using nested loops
        # --------------------------------------------------
        #
        # answer = []
        #
        # for i in range(len(nums)):
        #     leftSum = 0
        #     rightSum = 0
        #
        #     for j in range(len(nums)):
        #         if j < i:
        #             leftSum += nums[j]
        #         elif j > i:
        #             rightSum += nums[j]
        #
        #     answer.append(abs(leftSum - rightSum))
        #
        # return answer