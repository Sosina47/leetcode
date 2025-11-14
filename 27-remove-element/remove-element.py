class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        length = len(nums)
        for i in range(length):
            if nums[i] == val:
                count += 1
                nums[i] = '_'
        
        i, j = 0, 0
        while j < length and i < length:
            if nums[j] != '_' and j > i:
                if nums[i] == '_':
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                j += 1

        return length - count