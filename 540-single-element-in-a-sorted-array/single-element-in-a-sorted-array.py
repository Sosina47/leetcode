class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums) 

        if n == 1 or nums[0] != nums[1]: 
            return nums[0]

        for i in range(2, n - 1):
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]

        return nums[-1]