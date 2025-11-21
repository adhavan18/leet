class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c not in s:
                continue
            
            first = s.index(c)
            last = s.rindex(c)
            
            if first == last:
                continue
                
            middle = set(s[first+1:last])
            count += len(middle)
        
        return count
