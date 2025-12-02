class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        length = len(nums)

        if x > total:
            return -1
        
        if x == total:
            return length
        
        min_operation = float('inf')
        left = 0
        curr_sum = 0

        for right in range(length):
            curr_sum += nums[right]

            while total - curr_sum < x:
                curr_sum -= nums[left]
                left += 1 

            if total - curr_sum == x:
                min_operation = min(min_operation, length - (right - left + 1))
            
        return -1 if min_operation == float('inf') else min_operation