class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = count = 0
        max_length = float('-inf')
        for right in range(len(nums)):
            count += nums[right]

            while right - left + 1 - count > k:
                count -= nums[left]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length