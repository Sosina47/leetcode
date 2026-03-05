class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        nums = list(accumulate(nums))
        pos = defaultdict(int)
        pos[0] = 1
        count = 0

        for i in range(len(nums)):
            if nums[i] >= goal:
                count += pos[nums[i] - goal] 
                pos[nums[i]] += 1
            else:
                pos[nums[i]] += 1

        return count