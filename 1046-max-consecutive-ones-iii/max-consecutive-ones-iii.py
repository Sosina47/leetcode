class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        left = right = 0
        temp_k = k

        while right < len(nums):
            while temp_k == 0 and nums[right] == 0:
                if nums[left] == 0:
                    temp_k += 1
                left += 1
                
            if nums[right] == 0 and temp_k > 0:
                temp_k -= 1
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length