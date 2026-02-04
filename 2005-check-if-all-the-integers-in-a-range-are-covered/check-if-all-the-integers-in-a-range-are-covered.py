class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for rng in ranges:
            if left > right:
                return True
            
            if rng[0] <= left <= rng[1]:
                if rng[1] >= right:
                    return True
                
                left += rng[1] - left + 1

        return True if left > right else False