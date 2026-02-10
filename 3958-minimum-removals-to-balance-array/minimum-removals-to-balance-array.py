class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0

        nums.sort()
        max_nums = 0
        left, right = 0, 1

        while right < n:
            if nums[right] / nums[left] <= k:
                max_nums = max(max_nums, right - left + 1)
                right += 1
            else:
                left += 1

        nums.sort(reverse=True)
        left, right = 0, 1

        while right < n:
            if nums[left] / nums[right] <= k:
                max_nums = max(max_nums, right - left + 1)
                right += 1
            else:
                left += 1

        return n - max_nums