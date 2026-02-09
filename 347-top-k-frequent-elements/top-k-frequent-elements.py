class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = list(count.values())
        freq.sort(reverse=True)

        output = []

        for i in range(k):
            for key in count:
                if count[key] == freq[i]:
                    output.append(key)
                    del count[key]
                    break

        return output