class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []
        
        for i in range(n - k + 1):
            sub = nums[i:i+k]
            freq = Counter(sub)
            sorted_items = sorted(freq.items(), key = lambda p: (-p[1], -p[0]))

            top_x = [num for num, _ in sorted_items[:x]]
            s = sum(num * freq[num] for num in top_x)
            answer.append(s)

        return answer