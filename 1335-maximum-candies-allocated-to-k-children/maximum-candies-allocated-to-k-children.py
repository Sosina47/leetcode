class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)

        if total < k:
            return 0       
        
        n = len(candies)

        high = max(candies)
        low = 1

        def check(mid):
            count = 0

            for c in candies:
                count += c // mid

            return count >= k


        while high >= low:
            mid = (high + low) // 2

            if check(mid):
                low = mid + 1

            else:
                high = mid - 1
        
        return high 