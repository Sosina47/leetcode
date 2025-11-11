class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = [letter for letter in s]
        i, j = 0, len(s) - 1
        while i < j:
            if s_list[i] in vowels:
                if s_list[j] in vowels:
                    s_list[i], s_list[j] = s_list[j], s_list[i]
                    i += 1
                j -= 1
            else:
                if s_list[j] not in vowels:
                    j -= 1
                i += 1

        return ''.join(s_list)
    
