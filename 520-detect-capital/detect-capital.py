class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        wordLower = word.lower()
        wordUpper = word.upper()

        if word == wordLower:
            return True
        
        if word[0] != wordUpper[0]:
            return False
        
        is_Upper = True
        for i in range(1, len(word)):
            if word[i] != wordUpper[i]:
                is_Upper = False

        is_Lower = True
        for i in range(1, len(word)):
            if word[i] != wordLower[i]:
                is_Lower = False

        return is_Upper or is_Lower