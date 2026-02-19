class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        unique_nums = sorted(list(set(nums)))

        position = {val : i for i, val in enumerate(unique_nums)}
        prefix_sum = [0]

        for i in range(len(unique_nums)):
            unique_nums[i] = frequency[unique_nums[i]]
        
        for i in range(len(unique_nums)):
            prefix_sum.append(prefix_sum[-1] + unique_nums[i])

        for i in range(len(nums)):
            nums[i] = prefix_sum[position[nums[i]]]

        return nums