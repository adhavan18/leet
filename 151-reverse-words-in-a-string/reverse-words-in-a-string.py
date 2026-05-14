#class Solution:
 #   def reverseWords(self, s: str) -> str:
  #      words = s.split()
   #     res = []

    #    for i in range(len(words) - 1, -1, -1): #for ex: len(words) = 4 
     #   #-> for i in range()
      #      res.append(words[i])
       #     if i != 0:
        #        res.append(" ")
        #return"".join(res)
class Solution:
    def reverseWords(self, s: str) -> str:
        return" ".join(s.split()[::-1])