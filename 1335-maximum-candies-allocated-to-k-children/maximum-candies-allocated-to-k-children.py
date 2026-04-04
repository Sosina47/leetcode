class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        def check(mid):
            count = 0
            for i in range(len(candies)):
                count += candies[i] // mid

            return count >= k
                

        high = max(candies)
        low = 1

        while high >= low:
            mid = (high + low) // 2

            if check(mid):
                low = mid + 1

            else:
                high = mid - 1

        return high