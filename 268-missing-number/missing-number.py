# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         i = 0
#         while i < len(nums):
#             if nums[i] >= len(nums):
#                 i += 1
#                 continue
#             correct_index = nums[i]
#             if nums[i] != i:
#                 nums[i], nums[correct_index] = nums[correct_index], nums[i]
#             else:
#                 i += 1

#         for i in range(len(nums)):
#             if nums[i] != i:
#                 return i
        
#         # if there are 0 - n numbers, the missing is n
#         return len(nums)



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)

        for i in range(n + 1):
            if i not in nums:
                return i