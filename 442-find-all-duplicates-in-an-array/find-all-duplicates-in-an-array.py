from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                output.append(nums[i])

        return output