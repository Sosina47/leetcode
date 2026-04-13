class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        col = set()
        left = set()
        right = set()
        
        def solve(path):
            nonlocal col, left, right

            if len(path) == n:
                output.append(path[:])
                return 

            length = len(path) 

            for i in range(n):
                if i not in col and i - length not in right and i + length not in left:
                    col.add(i)
                    left.add(i + length)
                    right.add(i - length)

                    cur = ['Q' if j == i else '.' for j in range(n)]

                    path.append("".join(cur))

                    solve(path)

                    path.pop()
                    col.remove(i)
                    left.remove(i + length)
                    right.remove(i - length)

        solve([])
        return output

