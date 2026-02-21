class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        current = intervals[0]

        for i in range(1, len(intervals)):
            if i == len(intervals) - 1:
                if current[1] > intervals[i][0]:
                    count += 1

            else:
                if current[1] > intervals[i][0]:
                    if intervals[i][1] < current[1]:
                        current = intervals[i]
                        
                    count += 1
                else:
                    current = intervals[i]

        return count