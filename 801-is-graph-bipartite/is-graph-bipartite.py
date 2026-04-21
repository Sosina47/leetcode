class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                color[i] = 0

            stack = [i]

            while stack:
                index = stack.pop()
                
                for ch in graph[index]:
                    if color[ch] == -1:
                        color[ch] = color[index] ^ 1

                    elif color[ch] == color[index]:
                        return False

                    else:
                        continue

                    stack.append(ch)

                    
        return True