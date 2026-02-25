class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ = float('-inf')
        left = total = 0

        for right in range(len(nums)):
            total += nums[right]

            if right - left == k:
                total -= nums[left]
                left += 1

            if right - left == k - 1:
                max_ = max(max_, (total) / k)

        return max_