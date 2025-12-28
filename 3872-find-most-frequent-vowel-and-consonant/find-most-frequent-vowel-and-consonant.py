class Solution:
    def maxFreqSum(self, s: str) -> int:
        s_count = Counter(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowel = 0
        max_cons = 0

        for letter in s_count:
            if letter in vowels:
                max_vowel = max(max_vowel, s_count[letter])
            else:
                max_cons = max(max_cons, s_count[letter])

        return max_cons + max_vowel
    