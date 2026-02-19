class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)

        for right in range(2, len(nums)):
            if nums[right - 2] < nums[right - 1] + nums[right]:
                return sum(nums[right - 2 : right + 1])

        return 0