class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                nums.append(matrix[r][c])

        nums.sort()
        count = 0

        # for i in range(len(nums)):
        #     if i == 0 or nums[i] != nums[i - 1]:
        #     count += 1

        #     if count == k:
        #         return nums[i]

        return nums[k - 1]