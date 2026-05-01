class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        outdegree = [0] * n

        for i in range(len(edges)): 
            k, m = edges[i]
            outdegree[k] += 1

            adj[m].append(k)
            
        visited = [False] * n
        output = [[] for _ in range(n)]
        
        def dfs(i):
            if not adj[i]: 
                return [i]

            cur = []
            for val in adj[i]: 

                if visited[val]:
                    cur.extend(output[val])
                    cur.append(val)
                
                else:
                    visited[val] = True

                    cur.extend(dfs(val))
                    cur.append(val)

            output[i].extend(list(set(cur)))
            return cur
                
            
            
        for i in range(n): 
            if outdegree[i] == 0: 
                visited[i] = True

                dfs(i)

        res = [list(sorted(output[i])) for i in range(len(output))]
        return res