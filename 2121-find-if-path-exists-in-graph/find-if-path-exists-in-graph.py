class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        m = len(edges)

        adj_list = [[] for _ in range(n)]

        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        visited = [False] * n

        def dfs(node):
            if node == destination:
                return True

            visited[node] = True

            for child in adj_list[node]:
                if not visited[child]:
                    found = dfs(child)

                    if found:
                        return True
            
            return False

                        
        return dfs(source)