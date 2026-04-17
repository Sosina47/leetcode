class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target < row[0]:
                return False

            if target > row[-1]:
                continue

            left, right = 0, len(row)

            while right > left:
                mid = (right + left) // 2

                if row[mid] == target:
                    return True

                elif row[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return row[left] == target

        return False
            