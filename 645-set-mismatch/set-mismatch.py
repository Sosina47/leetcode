class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        double = -1
        missing = -1

        i = 0
        while i < len(nums):
            correct = nums[i] - 1

            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]

            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                
                double = nums[i]
                missing = i + 1
                break
            

        return double, missing