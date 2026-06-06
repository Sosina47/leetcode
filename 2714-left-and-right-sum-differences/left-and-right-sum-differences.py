class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = list(accumulate(nums))
        suffix = list(accumulate(nums[::-1]))[::-1]
        
        output = []
        for i in range(len(nums)):
            output.append(abs(prefix[i] - suffix[i] ))

        return output 