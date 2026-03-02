class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_ = nums[0]
        for i in range(1, len(nums)):
            if cur_sum + nums[i] < nums[i]:
                cur_sum = nums[i]
            
            else:
                cur_sum += nums[i]

            max_ = max(max_, cur_sum)

        return max_ 