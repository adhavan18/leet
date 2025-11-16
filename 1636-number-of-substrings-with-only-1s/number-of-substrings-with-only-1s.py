class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ones = 0
        result = 0

        for x in s:
            if x == '1':
                ones += 1
            else:
                result += ones * (ones + 1) // 2
                ones = 0

        result += ones * (ones + 1) // 2
        return result % MOD

