class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seenA = set()
        seenB = set()

        common = 0
        ans = []

        for i in range(len(A)):
            seenA.add(A[i])
            seenB.add(B[i])

            # if A[i] already existed in B
            if A[i] in seenB:
                common += 1

            # if B[i] already existed in A
            # avoid double counting
            if B[i] in seenA and A[i] != B[i]:
                common += 1

            ans.append(common)
        return ans