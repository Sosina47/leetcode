class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = math.ceil(len(nums) // 3)
        freq = Counter(nums)
        output = []
        for key, val in freq.items():
            if val > n:
                output.append(key)

        return output