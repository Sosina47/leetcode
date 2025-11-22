class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        countNoneDivisible = 0
        for num in nums:
            if num % 3 != 0:
                countNoneDivisible += 1

        return countNoneDivisible
        