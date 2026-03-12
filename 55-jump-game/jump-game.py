class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()
        jump = 1
        for i in range(1, len(nums)):
            if nums[i] >= jump:
                jump = 1
            else:
                jump += 1

        return True if jump == 1 else False