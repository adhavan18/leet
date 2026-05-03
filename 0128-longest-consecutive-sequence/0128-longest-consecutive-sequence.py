class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #constrain 1 = longest "consecutive" sequence
        #idc, if elements repeat
        n = set(nums) #fast lookup
        count = 0

        for i in n:
            if i - 1 not in n:
                curr = i
                current = 1
                while curr + 1 in n:
                    curr += 1
                    current += 1
                count = max(count, current)
        return count
        