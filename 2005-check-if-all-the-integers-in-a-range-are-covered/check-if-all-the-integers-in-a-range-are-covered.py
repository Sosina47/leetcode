class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for nums in range(left, right + 1):
            is_covered = False
            for interval in ranges:
                if interval[0] <= nums <= interval[1]:
                    is_covered = True
                    break
            if not is_covered:
                return False
            
        return True
    