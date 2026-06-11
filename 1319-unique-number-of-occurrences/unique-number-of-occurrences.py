class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = []
        for i in arr:
            c = arr.count(i)
            if c not in occ:
                occ.append(c)
        return len(occ) == len(set(arr))