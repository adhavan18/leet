class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        parent = {n: n for n in nums}
        size = {n: 1 for n in nums}
        
        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                size[root_j] += size[root_i]
                return size[root_j]
            return size[root_i]

        res = 1
        for n in nums:
            if n + 1 in parent:
                res = max(res, union(n, n + 1))
        return res