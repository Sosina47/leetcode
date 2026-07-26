class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        memo = defaultdict(list)

        def dp(i):
            if i in memo: 
                return memo[i]

            if i == n - 1: 
                memo[i].extend([nums[i], nums[i]])
                return memo[i]

            nxt = dp(i + 1)
            vals = (nums[i], nums[i] * nxt[0], nums[i] * nxt[1])

            memo[i].extend([max(vals), min(vals)])
            return memo[i]

        dp(0)
        mx = float("-inf")

        for mxx, _ in memo.values():
            mx = max(mx, mxx)

        return mx