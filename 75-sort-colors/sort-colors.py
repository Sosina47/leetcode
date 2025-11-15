class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 0  white, 1 white, 2 blue
        length = len(nums)
        left, right = 0, length - 1
        i = 0
        while i < length and i <= right:
            if nums[i] == 0 and left < i:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
