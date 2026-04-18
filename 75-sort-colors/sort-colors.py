class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j = 0, len(nums) - 1
        idx = 0

        while idx <= j:
            
            if nums[idx] == 0 and idx > i:
                nums[i], nums[idx] = nums[idx], nums[i]
                i += 1

            elif nums[idx] == 2:
                nums[j], nums[idx] = nums[idx], nums[j]
                j -= 1

            else:
                idx += 1
