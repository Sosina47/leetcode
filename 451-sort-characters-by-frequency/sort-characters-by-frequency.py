class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)

        freq = list(frequency.items())
        freq.sort(key=lambda x: x[1], reverse=True)

        output = []
        for key in freq:
            for i in range(key[1]):
                output.append(key[0])

        return ''.join(output)
        