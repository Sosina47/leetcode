class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i] + prefix[i - 1])

        for i in range(len(nums)):
            if total - prefix[i] == prefix[i] - nums[i]:
                return i
        return -1
    
