class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_removal = float('inf')
        length = len(nums)
        left = 0

        for right in range(length):
            while nums[right] > k * nums[left]:
                left += 1

            min_removal = min(min_removal, length - (right - left + 1))
        
        return min_removal