class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)] 
        depends = [0] * numCourses

        for i in range(len(prerequisites)):
            n, m = prerequisites[i]

            adj_list[m].append(n)
            depends[n] += 1

        q = deque()
        for i in range(numCourses): 
            if depends[i] == 0: 
                q.append(i)

        output = []
        while q:
            node = q.popleft()
            output.append(node)

            for val in adj_list[node]: 
                depends[val] -= 1

                if depends[val] == 0: 
                    q.append(val)
                    

        return output if len(output) == numCourses else []