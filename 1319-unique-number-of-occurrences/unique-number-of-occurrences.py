class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = []
        for i in arr:
            m = arr.count(i)
            if m not in c:
                c.append(m)
        return len(c) == len(set(arr))