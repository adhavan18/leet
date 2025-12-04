class Solution:
    def countCollisions(self, directions: str) -> int:
        #declare pointers i , j
        i = 0
        j = len(directions) - 1
        #remove L on the left side
        while i < len(directions) and directions[i] == 'L':
            i += 1
        while j >= 0 and directions[j] == 'R':
            j -= 1

        collisions = 0
        for c in directions[i:j+1]:
            if c != 'S':   
                collisions += 1
        
        return collisions