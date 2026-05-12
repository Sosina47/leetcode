class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = [[] for _ in range(len(isConnected))]

        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] == 1: 
                    adj[r].append(c)
                    adj[c].append(r)

        visited = [False]  * len(isConnected)
        count = 0
        
        for i in range(len(isConnected)):
            if not visited[i]: 
                count += 1

                q = deque([i])
                visited[i] = True

                while q: 
                    node = q.popleft()

                    for val in adj[node]: 
                        if not visited[val]: 
                            q.append(val)

                            visited[val] = True

        return count


