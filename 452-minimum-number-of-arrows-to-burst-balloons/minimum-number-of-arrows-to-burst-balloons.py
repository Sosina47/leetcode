class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        start = points[0]
        count_arrow = 0
        print(points)

        for i in range(1, len(points)):
            if points[i][0] > start[1]:
                count_arrow += 1
                start = points[i]

        count_arrow += 1

        return count_arrow