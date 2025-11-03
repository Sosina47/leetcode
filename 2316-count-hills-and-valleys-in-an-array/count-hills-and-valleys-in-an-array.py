class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        unique_nums = []
        for num in nums:
            if not unique_nums:
                unique_nums.append(num)
            elif num != unique_nums[-1]:
                unique_nums.append(num)
            else:
                continue
                
        count = 0
        for index in range(1, len(unique_nums) - 1):
            if unique_nums[index - 1] > unique_nums[index] < unique_nums[index + 1] or unique_nums[index - 1] < unique_nums[index] > unique_nums[index + 1]:
                count += 1

        return count