class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)
        return [num for num in nums_counter if nums_counter[num] == 2]
    