class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        dxn = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False] * m for _ in range(n)]
        
        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j):
            for dr, dc in dxn:
                nr, nc = i + dr, j + dc

                if inbound(nr, nc) and board[nr][nc] == 'O' and not visited[nr][nc]:
                    visited[nr][nc] = True

                    dfs(nr, nc)            

        for i in range(n):
            if i == 0 or i == n - 1:

                for j in range(m):
                    if board[i][j] == 'O' and not visited[i][j]:
                        visited[i][j] = True

                        dfs(i, j)

            else:
                if board[i][0] == 'O' and not visited[i][0]:
                    visited[i][0] = True

                    dfs(i, 0)

                if board[i][m - 1] == 'O' and not visited[i][m - 1]:
                    visited[i][m - 1] = True

                    dfs(i, m - 1)

        for i in range(1, n - 1):
            for j in range(1, m - 1):

                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'

        return board