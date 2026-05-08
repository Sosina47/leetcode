class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(-freq[key], key) for key in freq]

        heapify(heap)
        output = []

        for _ in range(k):
            output.append(heappop(heap)[1])

        return output