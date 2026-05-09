class Solution:
    def hammingWeight(self, n: int):
        b = ""
        while n > 0:
            remainder = n % 2
            b = str(remainder) + b
            n = n // 2
        count = 0
        for i in b:
            if i == "1":
                count += 1
        return count