class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        min_ = nums[0]

        for right in range(len(nums)):
            if nums[right] - min_ > k:
                count += 1
                min_ = nums[right]

        return count + 1