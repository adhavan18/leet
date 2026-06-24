class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
#from collections import Counter
#class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#        return Counter(s) == Counter(t)      

#class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#       if len(s) != len(t):
#           return False
#       count = {}
#       for ch in s:
#           count[ch] = count.get(ch, 0) + 1
#       for ch in t:
#           count[ch] = count.get(ch, 0) - 1
#       return all(v == 0 for v in count.vues())