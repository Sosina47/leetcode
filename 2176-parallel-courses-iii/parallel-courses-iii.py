class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n + 1)]
        visited = [-1] * (n + 1)
        outdegree = [0] * (n + 1)

        for before, next in relations: 
            adj[next].append(before)
            outdegree[before] += 1

        def dfs(i):
            if visited[i] != -1: 
                return visited[i]

            minn = 0

            for val in adj[i]:
                minn = max(minn, dfs(val))

            visited[i] = minn + time[i - 1]
            return minn + time[i - 1]
            
            

        output = 0

        for i in range(1, n + 1): 
            if visited[i] == -1 and outdegree[i] == 0:
                val = dfs(i)

                visited[i] = val

                if output == 0:
                    output += val

                else: 
                    output = max(output, val)

        return output