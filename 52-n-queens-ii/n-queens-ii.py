class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0

        col = set()
        left = set()
        right = set()

        def solve(path):
            nonlocal count, col, left, right

            if path == n:
                count += 1
                return 

            for i in range(n):
                if i not in col and i + path not in left and i - path not in right:
                    col.add(i)
                    left.add(i + path)
                    right.add(i - path)

                    solve(path + 1)

                    col.remove(i)
                    left.remove(i + path)
                    right.remove(i - path)

        solve(0)
        return count