class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        max_vowel = 0
        count_vowel = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for right in range(len(s)):
            if s[right] in vowels:
                count_vowel += 1

            if right - left + 1 > k:
                if s[left] in vowels:
                    count_vowel -= 1
                left += 1
            
            if right - left + 1 == k:
                max_vowel = max(max_vowel, count_vowel)

        return max_vowel
    