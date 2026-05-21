#class Solution:
#    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
#        ans = 0
#        for x in arr1:
#            for y in arr2:
#                a = str(x)
#                b = str(y)
#                count = 0
#                for i in range(min(len(a), len(b))):
#                    if a[i] == b[i]:
#                        count += 1
#                    else:
#                        break
#                ans = max(ans, count)
#        return ans
class Solution:
    def longestCommonPrefix(self, arr1, arr2):

        prefixes = set()

        # Store all prefixes from arr1
        for num in arr1:

            s = str(num)

            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        ans = 0

        # Check arr2 prefixes
        for num in arr2:

            s = str(num)

            for i in range(1, len(s) + 1):

                if s[:i] in prefixes:
                    ans = max(ans, i)

        return ans