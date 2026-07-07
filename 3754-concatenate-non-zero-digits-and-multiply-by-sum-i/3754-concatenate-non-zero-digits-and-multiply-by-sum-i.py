class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nonzero = ""
        digit_sum = 0

        for num in str(n):
            if num != '0':
                nonzero += num

        if nonzero == "":
            return 0

        for i in range(len(nonzero)):
            digit_sum += int(nonzero[i])

        return int(nonzero) * digit_sum