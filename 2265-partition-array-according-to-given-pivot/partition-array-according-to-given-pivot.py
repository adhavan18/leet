class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        equal = []
        greater = []
        for num in nums:
            if pivot > num:
                smaller.append(num)
            elif pivot < num:
                greater.append(num)
            else:
                equal.append(num)

        return smaller + equal + greater