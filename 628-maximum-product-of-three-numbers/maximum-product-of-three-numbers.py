class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse = True)

        if nums[0] > 0 and nums[-1] * nums[-2] >= nums[1] * nums[2]: 
            return nums[0] * nums[-1] * nums[-2]

        return nums[0] * nums[1] * nums[2]
         