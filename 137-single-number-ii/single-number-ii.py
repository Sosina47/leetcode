class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        for i in nums_counter:
            if nums_counter[i] == 1:
                return i
            