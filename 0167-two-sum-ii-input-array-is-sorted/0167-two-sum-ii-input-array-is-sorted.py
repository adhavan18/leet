class Solution:
    #def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #   n = len(numbers)
    #    for i in range(n):
    #        for j in range(i+1, n):
    #            if numbers[i] + numbers[j] == target:
    #                return [i+1,j+1]
    def twoSum(self, numbers, target):
        mp = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in mp:
                return [mp[complement] + 1, i + 1]
            mp[num] = i
