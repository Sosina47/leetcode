class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_pos = {0:-1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]

            if prefix % k in mod_pos:
                if i - mod_pos[prefix % k] > 1: 
                    return True
            else:
                mod_pos[prefix % k] = i
                
        return False