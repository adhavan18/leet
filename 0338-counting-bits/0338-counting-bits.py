#class Solution:
 #   def countBits(self, n: int) -> List[int]:
  #      ans = []
   #     for i in range(n + 1):
    #        if i == 0:
     #           ans.append(0)
      #      else:
       #         c = 0
        #        num = i
         #       while num > 0:
          #          if num % 2 == 1:
           #             c += 1
            #        num = num // 2
             #   ans.append(c)
        #return ans

class Solution:
    def countBits(self, n):
        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans