class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0] * (len(nums) + 1)
        for start, end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1

        prefix_sum = itertools.accumulate(prefix)
        prefix = list(prefix_sum)

        prefix.pop()
        prefix.sort(reverse=True)
        nums.sort(reverse=True)
        
        for i in range(len(prefix)):
            nums[i] *= prefix[i]
            
        return sum(nums) % (10 ** 9 + 7)
