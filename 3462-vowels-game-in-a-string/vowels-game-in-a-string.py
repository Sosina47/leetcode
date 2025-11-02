class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count_vowels = 0
        for letter in s:
            if letter in vowels:
                count_vowels += 1
        
        if count_vowels == 0:
            return False
        
        return True