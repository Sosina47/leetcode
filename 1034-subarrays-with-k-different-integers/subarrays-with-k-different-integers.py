class Solution:
    def subarrays(self, nums, k):
        freq = defaultdict(int)
        left = count = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while len(freq) > k:
                if freq[nums[left]] == 1:
                    del freq[nums[left]]
                else:
                    freq[nums[left]] -= 1
                left += 1

            count += right - left + 1

        return count
            
            

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarrays(nums, k) - self.subarrays(nums, k - 1)