# from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 2
        length = len(nums)
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                j += 1
            else:
                nums.pop(j)
        return len(nums)

prob = Solution()
nums = [0,0,1,1,1,1,2,3,3]
print(prob.removeDuplicates(nums))
print(nums)
