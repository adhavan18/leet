class Solution:
    def maxDotProduct(self, a: List[int], b: List[int]) -> int:
        for a,b in (a,b),(b,a):
            if all(v<0 for v in a) and all(v>0 for v in b): return max(a)*min(b)

        return (f:=cache(lambda i,j:i<len(a) and j<len(b) 
            and max(a[i]*b[j]+f(i+1,j+1),f(i+1,j),f(i,j+1))))(0,0)