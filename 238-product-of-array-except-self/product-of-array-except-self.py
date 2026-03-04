class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = nums.count(0)
        if count >= 2:
            return [0] * len(nums)

        elif count == 1:
            product = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    product *= nums[i]
            
            return [0 if nums[i] else product for i in range(len(nums))]

        else:
            product = reduce(lambda x, y: x * y, nums)

            return [product // nums[i] for i in range(len(nums))]