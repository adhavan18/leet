from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        arr = sorted(Counter(word).values(), reverse = True)
        push = 0
        for i in range(len(arr)):
            push += arr[i] * (i // 8 + 1)
        return push
