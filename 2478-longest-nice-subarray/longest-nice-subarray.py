class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        bitwise = 0
        max_length = 0

        for right in range(len(nums)):
            while bitwise & nums[right] != 0:
                bitwise ^= nums[left]
                left += 1

            bitwise = bitwise ^ nums[right]
            max_length = max(max_length, right - left + 1) 
        
        return max_length
                