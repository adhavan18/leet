class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones = 0
        n = len(s)
        for i, c in enumerate(s):
            if c == '1':
                ones += 1
            elif i == n - 1 or s[i + 1] == '1':
                ans += ones
        return ans