class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        depends = defaultdict(int)

        for i in range(len(prerequisites)):
            n, m = prerequisites[i]

            adj_list[m].append(n)
            depends[n] += 1

        for i in range(numCourses): 
            depends[i]
        
        
        q = deque()
        for key in depends: 
            if depends[key] == 0: 
                q.append(key)

        output = []
        while q:
            node = q.popleft()
            output.append(node)

            for val in adj_list[node]: 
                if depends[val] == 1: 
                    q.append(val)
                else: 
                    depends[val] -= 1

        return output if len(output) == numCourses else []