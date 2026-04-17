class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1

        while high >= low:
            mid = (high + low) // 2

            if matrix[mid][0] <= target:
                low = mid + 1

            else:
                high = mid - 1

        if high == -1 or matrix[high][-1] < target:
            return False

        
        left, right = 0, len(matrix[high])

        while left < right:
            mid = (right + left) // 2
            
            if matrix[high][mid] == target:
                return True

            elif matrix[high][mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return matrix[high][right] == target
