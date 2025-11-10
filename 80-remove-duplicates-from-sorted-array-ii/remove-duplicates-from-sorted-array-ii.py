class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 2
        while j < len(nums):
            if nums[i] == nums[j]:
                nums[i] = '_'
            i += 1
            j += 1
        
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != '_':
                if nums[i] == '_':
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

        return i
                