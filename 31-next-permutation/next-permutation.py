class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        pivot = -1

        for i in range(length - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break

        if pivot == -1:
            nums.sort()
            return nums

        right = -1
        for i in range(pivot + 1, length):
            if nums[i] <= nums[pivot]:
                right = i - 1 
                break

        nums[pivot], nums[right] = nums[right], nums[pivot]

        left = pivot + 1
        right = length - 1

        while right > left:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1

        return nums
