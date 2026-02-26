class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        total = left = max_len = 0
        is_deleted = False
        for right in range(len(nums)):
            total += nums[right]

            while total + 1 < right - left + 1:
                if nums[left]:
                    total -= 1
                
                left += 1
            
            if total + 1 == right - left + 1:
                is_deleted = True

            max_len = max(max_len, total)
        
        if not max_len: 
            return 0

        return max_len if is_deleted else max_len - 1