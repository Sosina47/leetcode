class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        num = min(itertools.accumulate(nums))
        if num <= 0:
            return 1 - num
        else:
            return 1