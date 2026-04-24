class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        visited = [False] * n
        output = []

        def dfs(node, path): 
            if node == n-1:
                output.append(path[:])
                return 

            for val in graph[node]:
                path.append(val)

                dfs(val, path)

                path.pop()


        dfs(0, [0])

        return output
        