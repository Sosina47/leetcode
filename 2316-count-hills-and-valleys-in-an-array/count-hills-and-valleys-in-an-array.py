class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums) - 1):
            left = i - 1
            if nums[left] == nums[i]:
                continue

            right = i + 1
            if nums[right] == nums[i]:
                while right < len(nums) - 1:
                    right += 1
                    if nums[right] != nums[i]:
                        break
            if nums[right] == nums[i]:
                continue
            
            if (nums[i] > nums[left] and nums[i] > nums[right]) or (nums[i] < nums[left] and nums[i] < nums[right]):
                count += 1

        return count