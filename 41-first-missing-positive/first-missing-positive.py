class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums):
            if nums[index] <= 0 or nums[index] > len(nums):
                index += 1
                continue
            correct = nums[index] - 1
            if nums[index] != nums[correct]:
                nums[index], nums[correct] = nums[correct], nums[index]
            else:
                index += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
    