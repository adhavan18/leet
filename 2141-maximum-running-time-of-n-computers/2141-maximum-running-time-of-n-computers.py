class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        pass
        left, right = 0, sum(batteries) // n
        while left < right:
            mid = (left + right + 1) // 2
            total = sum(min(b, mid) for b in batteries)
            
            if total >= n * mid:
                left = mid
            else:
                right = mid - 1
        
        return left