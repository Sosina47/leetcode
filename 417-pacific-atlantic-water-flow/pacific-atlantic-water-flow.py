class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        visited_a = [[False] * m for _ in range(n)]
        visited_p = [[False] * m for _ in range(n)]

        dxn = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        pac = [[False] * m for _ in range(n)]
        atl = [[False] * m for _ in range(n)]

        def inbound(i, j): 
            return 0 <= i < n and 0 <= j < m

        def pac_dfs(i, j):
            if i == 0 or j == 0: 
                return True
            
            for dr, dc in dxn: 
                nr, nc = i + dr, j + dc

                if not inbound(nr, nc) or heights[nr][nc] > heights[i][j]: 
                    continue

                if visited_p[nr][nc]: 
                    if pac[nr][nc]: 
                        return True

                else: 
                    visited_p[nr][nc] = True
                    if pac_dfs(nr, nc): 
                        pac[nr][nc] = True
                        return True
                    
                    else: 
                        visited_p[nr][nc] = False

            return False
            
            

        def atl_dfs(i, j):
            if i == n - 1 or j == m - 1: 
                return True

            for dr, dc in dxn: 
                nr, nc = i + dr, j + dc

                if not inbound(nr, nc) or heights[nr][nc] > heights[i][j]: 
                    continue

                if visited_a[nr][nc]: 
                    if atl[nr][nc]: 
                        return True

                else: 
                    visited_a[nr][nc] = True
                    if atl_dfs(nr, nc): 
                        atl[nr][nc] = True
                        return True
                    
                    else:
                        visited_a[nr][nc] = False
                        

            return False

        output = []
        
        for i in range(n): 
            for j in range(m):

                # if visited_p[i][j]:
                #     if pac[i][j] and atl[i][j]: 
                #         output.append([i, j])
                    
                # else:
                    visited_p[i][j] = True
                    visited_a[i][j] = True

                    p = pac_dfs(i, j)
                    a = atl_dfs(i, j)
                    
                    if p and a:
                        output.append([i, j])

                    pac[i][j] = p
                    atl[i][j] = a

        return output

                

                