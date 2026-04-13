class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = set()
        col = []
        left = []
        right = []
        
        def solve(path):
            nonlocal col, left, right

            if len(path) == n:
                output.add(tuple(path[:]))
                return 

            length = len(path) 

            for i in range(n):
                if i not in col and i - length not in right and i + length not in left:
                    col.append(i)
                    left.append(i + length)
                    right.append(i - length)

                    cur = ['Q' if j == i else '.' for j in range(n)]

                    path.append("".join(cur))

                    solve(path)

                    path.pop()
                    col.pop()
                    left.pop()
                    right.pop()

        solve([])
        return list(output)

