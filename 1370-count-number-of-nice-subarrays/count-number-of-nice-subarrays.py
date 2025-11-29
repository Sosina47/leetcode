class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = 0
        result = 0

        left = mid = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd += 1

            while odd > k:
                if nums[left] % 2 == 1:
                    odd -= 1                
                left += 1
                mid = left
                

            if odd == k:
                while nums[mid] % 2 == 0:
                    mid += 1
                valid_start = (mid - left) + 1
                result += valid_start

        return result