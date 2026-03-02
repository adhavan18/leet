class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        #check number of zeroes in each row>
        zeroes = []
        n = len(grid)
        
        for row in grid:
            count = 0
            for j in range(n-1,-1,-1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            zeroes.append(count)
        
        swaps = 0

        for i in range(n):
            required = n - 1 - i

            j = i
            while j < n and zeroes[j] < required:
                j += 1
    
            if j == n:
                return -1
    
            # bubble up
            while j > i:
                zeroes[j], zeroes[j-1] = zeroes[j-1], zeroes[j]
                swaps += 1
                j -= 1

        return swaps