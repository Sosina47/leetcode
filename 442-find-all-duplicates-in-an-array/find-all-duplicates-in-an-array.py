
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        index = 0
        while index < len(nums):
            correct = nums[index] - 1
            if nums[index] != nums[correct]:
                nums[index], nums[correct] = nums[correct], nums[index]
            else:
                index += 1

        duplicates = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicates.append(nums[i])
    
        return list(set(duplicates))
