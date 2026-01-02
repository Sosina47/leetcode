class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = set(sentence)
        for i in range(97, 97 + 26):
            if chr(i) not in sentence:
                return False
                
            
        return True