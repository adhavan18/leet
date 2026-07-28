class Solution:
    def smallestPalindrome(self, s: str):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        left = ""
        middle = ""
        for ch in sorted(freq.keys()):
            left += ch * (freq[ch] // 2)
            if freq[ch] % 2 == 1:
                middle = ch
        ans = left + middle + left[::-1]
        return ans