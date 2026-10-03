class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        stack = [-1]
        max_length = 0
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            else:
                stack.pop()
#see, you first check if it starts with ), then automatically, its 0
#if, it starts with "(" then we'd take any "()" and count as 2
#return total count
                if len(stack) == 0:
                    stack.append(index)
                else:
                    current_length = index - stack[-1]
                    max_length = max(max_length, current_length)
        return max_length

            
        

