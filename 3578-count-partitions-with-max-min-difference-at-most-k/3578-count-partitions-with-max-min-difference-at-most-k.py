from collections import deque

M = 10**9 + 7

class Solution:
    def countPartitions(self, nums, k) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        pre = [0] * (n + 1)

        dp[0] = 1
        pre[0] = 1

        maxQ = deque()
        minQ = deque()
        L = 0

        for i in range(n):
            # maintain decreasing max queue
            while maxQ and nums[maxQ[-1]] <= nums[i]:
                maxQ.pop()
            maxQ.append(i)

            # maintain increasing min queue
            while minQ and nums[minQ[-1]] >= nums[i]:
                minQ.pop()
            minQ.append(i)

            # shrink window until max - min <= k
            while nums[maxQ[0]] - nums[minQ[0]] > k:
                if maxQ[0] == L:
                    maxQ.popleft()
                if minQ[0] == L:
                    minQ.popleft()
                L += 1

            # dp[i+1] = sum(dp[L..i])
            dp[i + 1] = (pre[i] - (pre[L - 1] if L > 0 else 0)) % M
            pre[i + 1] = (pre[i] + dp[i + 1]) % M

        return dp[n]
