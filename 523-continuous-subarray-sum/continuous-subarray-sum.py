class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        mod_map = {nums[0] % k: 0}

        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        for i in range(1, len(prefix_sum)):
            if prefix_sum[i] % k == 0:
                print(prefix_sum[i])
                return True

            mod = prefix_sum[i] % k
            if mod in mod_map:
                
                if mod_map[mod] + 2 <= i:
                    return True
            
            else:
                mod_map[prefix_sum[i] % k] = i     

        return False 
                