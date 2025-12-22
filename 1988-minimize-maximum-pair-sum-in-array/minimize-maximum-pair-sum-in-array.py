class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        left = 0
        right = len(nums)-1
        while right > left:
            max_sum = max(max_sum, nums[right] + nums[left])
            right -= 1
            left += 1
        
        return max_sum