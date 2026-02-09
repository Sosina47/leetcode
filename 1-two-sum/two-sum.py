class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            if target - nums[i] in idx and i != idx[target - nums[i]]:
                return (i, idx[target - nums[i]])
































        # prefix = [0] * len(nums)
        # pos = {0: -1}

        # for i in range(len(nums)):
        #     if i == 0:
        #         prefix[i] = nums[i]
        #     else:
        #         prefix[i] = nums[i] + prefix[i - 1]
            
        #     if prefix[i] - target in pos:
        #         return [pos[prefix[i] - target] + 1, i]

        #     pos[prefix[i]] = i