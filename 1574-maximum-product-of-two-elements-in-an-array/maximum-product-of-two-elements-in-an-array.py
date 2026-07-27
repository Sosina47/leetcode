class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = mx2 = 0

        for i in range(len(nums)):
            if nums[i] > mx: 
                mx2 = mx
                mx = nums[i]

            elif nums[i] > mx2: 
                mx2 = nums[i]


        return (mx - 1) * (mx2 - 1)