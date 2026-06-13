class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ''

        for word in words:
            weight = 0

            for c in word:
                pos = ord(c) % 97
                weight += weights[pos]

            weight %= 26
            weight = (weight - 25) * -1
            
            res += chr(weight + 97)

        return res