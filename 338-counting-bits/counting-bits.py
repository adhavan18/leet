#class Solution:
 #   def countBits(self, n: int) -> List[int]:
  #      count = []
   #     for i in range(n + 1):
    #        if i == 0:
     #           count.append(0)
      #      else:
       #         c = 0
        #        num = i
         #       while num > 0:
          #          if num % 2 == 1:
           #             c += 1
            #        num = num // 2
             #   count .append(c)
        #return count
from typing import List
class Solution:
    def countBits(self, n):
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
        