class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)] 

        for i in range(len(prerequisites)):
            n, m = prerequisites[i]

            adj_list[n].append(m)

        visited = [-1] * numCourses
        output = []

        def dfs(i): 
            for val in adj_list[i]: 
                if visited[val] == 2:
                    continue

                if visited[val] == 1: 
                    return False

                visited[val] = 1
                if not dfs(val):
                    return False

            visited[i] = 2
            output.append(i)

            return True


        for i in range(numCourses): 
            if visited[i] != 2: 
                if not dfs(i): 
                    return []

        return output