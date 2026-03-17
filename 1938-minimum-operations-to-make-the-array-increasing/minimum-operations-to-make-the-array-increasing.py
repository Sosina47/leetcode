class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        cur = nums[0] + 1

        for num in nums[1:]:
            if num >= cur:
                cur = num + 1
            else:
                operations += cur - num
                cur += 1
        
        return operations