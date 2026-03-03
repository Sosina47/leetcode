class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pos = {0: -1}
        count = 0
        total = 0

        for i in range(len(nums)):
            total += 1 if nums[i] else -1 
        
            if total in pos:
                count = max(count, i - pos[total])
            else:
                pos[total] = i

        return count