class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in range(len(strs[0])):
            first = strs[0][col]
            for row in range(1, len(strs)):
                if ord(strs[row][col]) < ord(first):
                    count += 1
                    break
                first = strs[row][col]

        return count