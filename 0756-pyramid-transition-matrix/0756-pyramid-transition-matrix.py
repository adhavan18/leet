class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict
        from functools import lru_cache 
        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[a+b].append(c)
        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True

            def backtrack(i, next_row):
                if i == len(row) - 1:
                    return dfs(next_row)

                pair = row[i:i+2]
                if pair not in mp:
                    return False

                for ch in mp[pair]:
                    if backtrack(i + 1, next_row + ch):
                        return True

                return False

            return backtrack(0, "")

        return dfs(bottom)
        