class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True) # should first assign the larger ones (minimizes the runtime)
        
        length = len(cookies)
        min_unfair = float("inf")
        
        def solve(start, nums):
            nonlocal min_unfair

            if start == length:
                min_unfair = min(min_unfair, max(nums))
                return 

            for i in range(k):
                # u already tried giving the current cookie with a child the same # cookies
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                    
                nums[i] += cookies[start]

                if nums[i] < min_unfair:
                    solve(start + 1, nums)
                
                nums[i] -= cookies[start]

                # if the current kid got 0 cookies, the rest of the kids after him also have 0 cookies. and if we try   assigning a cookie to him and if it didn't work, then it won't work for the rest of the kids who got 0 cookies like him
                if nums[i] == 0:
                    break

        solve(0, [0] * k)
        return min_unfair 