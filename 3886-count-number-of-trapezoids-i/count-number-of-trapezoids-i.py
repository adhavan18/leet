class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        M = 10**9 + 7

        count = defaultdict(int)
        for x,y in points:
            count[y] += 1
        choose = []
        for c in count.values():
            if c >= 2:
                choose.append(c * (c - 1) // 2)
        
        S = sum(choose) % M
        S2 = sum(x * x for x in choose) % M
        inv2 = pow(2, M-2, M)
        ans = ((S * S - S2) % M) * inv2 % M

        return ans % M
