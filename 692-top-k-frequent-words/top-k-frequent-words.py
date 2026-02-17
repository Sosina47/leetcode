class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency_table = Counter(words)
        pairs = list(frequency_table.items())
        pairs.sort(key = lambda x: (-x[1], x[0]))

        output = []
        for i in range(k):
            output.append(pairs[i][0])

        return output