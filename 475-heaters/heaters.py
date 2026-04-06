class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
            houses.sort()
            heaters.sort()
            
            n = len(houses)
            m = len(heaters)

            def check(mid):
                idx = 0

                for i in range(n):
                                            
                    while abs(houses[i] - heaters[idx]) > mid:
                        if idx == m - 1:
                            return False

                        idx += 1
                
                return True
            

            high = max(abs(houses[-1] - heaters[-1]), abs(houses[0] - heaters[-1]))
            low = 0

            while high >= low:
                mid = low + (high - low) // 2

                if check(mid):
                    high = mid - 1

                else:
                    low = mid + 1

            return low

            
            