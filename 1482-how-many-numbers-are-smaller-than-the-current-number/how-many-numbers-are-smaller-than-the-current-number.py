class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        dictNums = {}
        for i in range(len(sortedNums)):
            num = sortedNums[i]
            if num not in dictNums:
                dictNums[num] = i
                
        for i in range(len(nums)):
            nums[i] = dictNums[nums[i]]

        return nums




