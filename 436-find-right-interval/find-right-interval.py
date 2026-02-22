class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        length = len(intervals)
        for i in range(length):
            intervals[i].append(i)

        intervals.sort()
        output = [-1] * length

        for i in range(length):
            left = 0
            right = length - 1

            while right >= left:
                mid = (right + left) // 2
                if intervals[mid][0] >= intervals[i][1]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            if left < length:
                output[intervals[i][2]] = intervals[left][2]           
            
        return output 