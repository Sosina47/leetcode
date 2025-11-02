class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count_vowels = 0
        for letter in s:
            if letter in vowels:
                return True
        
        return False