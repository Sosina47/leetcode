class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = set()

        i = 0
        while i < len(nums):
            if nums[i] == i + 1:
                i += 1

            else:
                correct = nums[i] - 1

                if nums[i] == nums[correct]:
                    output.add(nums[i])
                    i += 1

                else:
                    nums[i], nums[correct] = nums[correct], nums[i]

        return list(output)