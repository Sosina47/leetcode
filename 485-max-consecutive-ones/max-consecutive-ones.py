class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        max_ones = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1
            else:
                max_ones = max(max_ones, right - left + 1)

        return max_ones