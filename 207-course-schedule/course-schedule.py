class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)] 

        for i in range(len(prerequisites)):
            a, b = prerequisites[i]

            adj_list[a].append(b)

        color = [-1 for _ in range(numCourses)] 
        
        def dfs(i):
            if not adj_list[i] or color[i] == 2:
                return True

            if color[i] == 1:
                return False

            color[i] = 1
            
            for val in adj_list[i]:
                if not dfs(val):
                    return False

            color[i] = 2
            return True

        for i in range(numCourses):
            if not adj_list[i] or color[i] == 2:
                continue

            color[i] = 1

            for val in adj_list[i]:
                if not dfs(val):
                    return False
            
            color[i] = 2
            
        return True