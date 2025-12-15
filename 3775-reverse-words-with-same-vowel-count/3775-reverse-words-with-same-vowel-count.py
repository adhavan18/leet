class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        def count_vowels(word):
            return sum(1 for char in word if char in vowels)

        words = s.split()

        vowel_count = count_vowels(words[0])

        for i in range(1, len(words)): 
            if count_vowels(words[i]) == vowel_count:
                words[i] = words[i][::-1] 
        
        return ' '.join(words)