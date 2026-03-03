class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i - 1])

        seen = defaultdict(int)
        seen[0] += 1
        count = 0
        for i in range(len(prefix)):
            if prefix[i] % k in seen:
                count += seen[prefix[i] % k]
            seen[prefix[i] % k] += 1

        return count
