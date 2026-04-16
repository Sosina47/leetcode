class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            if nums[i] == i + 1:
                i += 1

            else:
                correct = nums[i] - 1
                if nums[correct] == nums[i]:
                    return nums[i]

                nums[i], nums[correct] = nums[correct], nums[i]

        