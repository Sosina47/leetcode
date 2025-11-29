class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] + prefix[i - 1] 

        return prefix