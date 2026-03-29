class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        length = len(cookies)
        min_unfair = float("inf")
        
        def solve(start, nums):
            nonlocal min_unfair

            if start == length:
                min_unfair = min(min_unfair, max(nums))
                return 

            for i in range(k):
                nums[i] += cookies[start]

                solve(start + 1, nums)
                
                nums[i] -= cookies[start]

        solve(0, [0] * k)
        return min_unfair 