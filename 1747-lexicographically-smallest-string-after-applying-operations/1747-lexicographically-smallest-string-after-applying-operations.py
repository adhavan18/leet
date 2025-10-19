from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        q = deque([s])
        ans = s
        n = len(s)

        while q:
            cur = q.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            ans = min(ans, cur)

            # Operation 1: add a to all digits at odd indices
            arr = list(cur)
            for i in range(1, n, 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            added = ''.join(arr)
            if added not in seen:
                q.append(added)

            # Operation 2: rotate right by b
            rotated = cur[-b:] + cur[:-b]
            if rotated not in seen:
                q.append(rotated)

        return ans