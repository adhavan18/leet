class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        ones = sum(1 for x in nums if x == 1) #count ones
        if ones > 0:                          #if we have ones
            return n - ones             

        min_len = float('inf')

        for i in range(n):
            g = nums[i]

            if g == 1:
                
                min_len = 1
                break
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
                        
        if min_len == float('inf'):
            return -1

        return (n - 1) + (min_len - 1)
        