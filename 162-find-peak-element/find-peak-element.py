class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0 
        left, mid = 0, 1
        for i in range(2, n):
            if nums[left] < nums[mid] > nums[i]:
                return mid
            left, mid = mid, i

        if nums[n-1] > nums[n-2]:
            return n - 1
        return 