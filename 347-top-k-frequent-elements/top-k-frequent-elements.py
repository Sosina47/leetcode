class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = list(count.items())
        freq.sort(key=lambda x: x[1], reverse=True)
        
        output = []

        for i in range(k):
            output.append(freq[i][0])

        return output