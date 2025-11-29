class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_start_value = 1
        startValue = 0
        for i in range(len(nums)):
            startValue += nums[i] 
            if startValue < 1:
                min_start_value = max(min_start_value, 1 - startValue)
            
        return min_start_value
    