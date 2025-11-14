class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        max_height = max(heights)
        count = [0] * (max_height + 1)
        for i in range(len(heights)):
            count[heights[i]] += 1

        expected = []
        for i in range(len(count)):
            for j in range(count[i]):
                expected.append(i)

        count_mismatch = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                count_mismatch += 1

        return count_mismatch