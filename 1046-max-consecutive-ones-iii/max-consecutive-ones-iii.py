class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        count_zeros = 0
        max_length = 0

        while right < len(nums):
            if nums[right] == 0:
                count_zeros += 1
            
            while count_zeros > k:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length