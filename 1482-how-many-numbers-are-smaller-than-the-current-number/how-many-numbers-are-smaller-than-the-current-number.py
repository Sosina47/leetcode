class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        sorted_dict = {}
        for i in range(len(sorted_nums)):
            num = sorted_nums[i]
            if num not in sorted_dict:
                sorted_dict[num] = i

        for i in range(len(nums)):
            num = nums[i]
            nums[i] = sorted_dict[num]
        
        return nums