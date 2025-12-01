class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        # for left in range(len(nums)):
        #     curr_length = 0
        #     total = 0
        #     for right in range(left, len(nums)):
        #         total += nums[right]
        #         if total == target:
        #             min_length = min(min_length, right - left + 1)
        #             break


        left = 0
        curr_length = 0
        total = 0

        for right in range(len(nums)):
            total += nums[right] 

            while target <= total:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1        
                
            # if total >= target:
            #     curr_length = right - left + 1
            #     min_length = min(min_length, curr_length)
            
        if min_length == float('inf'):
            return 0
        return min_length