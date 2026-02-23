class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p = 0
        for s in range(len(nums)):
            if nums[s] != 0:
                nums[p], nums[s] = nums[s], nums[p]
                p += 1
        