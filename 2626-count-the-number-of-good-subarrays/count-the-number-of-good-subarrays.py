class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = left = cur = 0
        freq = defaultdict(int)
        length = len(nums)

        for right in range(length):
            cur += freq[nums[right]]
            freq[nums[right]] += 1
            
            while cur >= k:
                count += length - right
                cur -= freq[nums[left]] - 1
                freq[nums[left]] -= 1
                left += 1              

        return count 




