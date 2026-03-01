class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(len(word)):
            chars = set()
            for j in range(i, len(word)):
                if word[j] in vowels:
                    chars.add(word[j])
                else:
                    break

                if len(chars) == 5:
                    count += 1

        return count