class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = [(-freq[key], key) for key in freq]

        heapify(heap)
        output = []

        for _ in range(k):
            output.append(heappop(heap)[1])

        return output