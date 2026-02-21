class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
      
        prime_count = 0
        for current_num in range(1, n):
            if is_prime[current_num]:
                prime_count += 1

                for multiple in range(current_num * 2, n, current_num):
                    is_prime[multiple] = False

        return prime_count