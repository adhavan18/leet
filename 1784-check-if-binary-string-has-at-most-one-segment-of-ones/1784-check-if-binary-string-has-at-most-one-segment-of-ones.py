class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        return "01" not in s

        #seen_zero = False

        #for c in s:
            #if c == '0':
            #    seen_zero = True
            #elif seen_zero:
            #    return False

        #return True