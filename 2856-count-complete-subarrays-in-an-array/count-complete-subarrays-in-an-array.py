class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = left = 0
        distinict = len(set(nums))
        cur = defaultdict(int)

        for right in range(len(nums)):
            cur[nums[right]] += 1

            while len(cur) == distinict:
                count += len(nums) - right                
                cur[nums[left]] -= 1

                if cur[nums[left]] == 0:
                    del cur[nums[left]]
                left += 1

        return count