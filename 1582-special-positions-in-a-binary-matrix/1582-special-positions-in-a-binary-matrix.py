class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0
        a = len(mat)
        b = len(mat[0])

        for row in range(a):
            for col in range(b):
                if mat[row][col] == 0:
                    continue
                
                good = True
                for r in range(a):
                    if r != row and mat[r][col] == 1:
                        good = False
                        break
                    
                for c in range(b):
                    if c != col and mat[row][c] == 1:
                        good = False
                        break
                
                if good:
                    result += 1
                    
        return result