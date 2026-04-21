class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        color = [-1] * n

        def dfs(i):
            for ch in graph[i]:
                if color[ch] != -1 and color[ch] ^ 1 != color[i]:
                    return False

                if color[ch] == -1:
                    color[ch] = color[i] ^ 1
                
                elif color[ch] ^ 1 == color[i]:
                    continue

                if not dfs(ch):
                    return False
            return True
            

        for i in range(n):
            if color[i] == -1:
                color[i] = 0

            for ch in graph[i]:
                if color[ch] != -1 and color[ch] ^ 1 != color[i]:
                    return False

                if color[ch] == -1:
                    color[ch] = color[i] ^ 1
                
                elif color[ch] ^ 1 == color[i]:
                    continue

                if not dfs(ch):
                    return False

        return True