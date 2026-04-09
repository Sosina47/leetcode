class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxx = 0

        for i in range(len(words)):
            word = words[i]
            n = len(word)

            for j in range(i + 1, len(words)):
                m = len(words[j])

                if not set(word) & set(words[j]):
                    maxx = max(maxx, n * m)
        
        return maxx