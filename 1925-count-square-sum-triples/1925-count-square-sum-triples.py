class Solution:
    def countTriples(self, n: int) -> int:
        import math
        count = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                value = a*a + b*b
                c = math.isqrt(value)
                if c * c == value and c <= n:
                    count += 1
        return count