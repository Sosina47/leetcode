class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def check(mid):
            count = 1
            prev = position[0]

            for i in range(1, n):                
                if position[i] - prev >= mid:
                    count += 1
                    prev = position[i]

            return count >= m


        low = 0
        high = 10 ** 9 - 1

        while high >= low:
            mid = low + (high - low) // 2

            if check(mid):
                low = mid + 1

            else:
                high = mid - 1

        return high