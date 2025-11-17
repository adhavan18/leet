class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        previous = -1
        for index, value in enumerate(nums):
            if value == 1:
                if previous == -1:
                    previous = index
                else:
                    if index - previous - 1 < k:
                        return False
                    previous = index

        return True