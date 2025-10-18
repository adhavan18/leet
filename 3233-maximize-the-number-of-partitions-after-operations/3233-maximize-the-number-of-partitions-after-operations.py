class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        from functools import lru_cache
        def bits(x):
            return bin(x).count("1")
        n = len(s)
        arr = [ord(c) - 97 for c in s]
        @lru_cache(None)
        def dfs(i, mask, changed):
            if i == n:
                return 1 if mask else 0
            res = 0
            c = arr[i]
            new_mask = mask | (1 << c)
            if bits(new_mask) > k:
                res = max(res, 1 + dfs(i + 1, 1 << c, changed))
            else:
                res = max(res, dfs(i + 1, new_mask, changed))
            if not changed:
                for ch in range(26):
                    if ch == c:
                        continue
                    new_mask2 = mask | (1 << ch)
                    if bits(new_mask2) > k:
                        res = max(res, 1 + dfs(i + 1, 1 << ch, True))
                    else:
                        res = max(res, dfs(i + 1, new_mask2, True))
            return res
        return dfs(0, 0, False)