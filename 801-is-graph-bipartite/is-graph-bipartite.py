class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = defaultdict(lambda : -1)

        for i in range(len(graph)): 
            que = deque([i])

            if color[i] == -1:
                color[i] = 1
                
                while que: 
                    node = que.popleft()

                    for n in graph[node]: 
                        if color[n] != -1 and color[n] != color[node] ^ 1: 
                            return False

                        if color[n] == -1: 
                            color[n] = color[node] ^ 1
                            que.append(n)

        return True 