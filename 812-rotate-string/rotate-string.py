class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        start = s
        if len(start) != len(goal):
            return False
        
        for _ in range(len(start)):
            start = start[1:] + start[0]
            if start == goal:
                return True
        return False
        