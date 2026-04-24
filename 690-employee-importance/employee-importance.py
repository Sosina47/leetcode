"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj_list = defaultdict(list)

        for e in employees:
            adj_list[e.id].append(e.importance)
            adj_list[e.id].append(e.subordinates)        
        
        que = deque()
        que.append(id)
        total = 0

        while que:
            i = que.popleft()

            total += adj_list[i][0]

            for n in adj_list[i][1]: 
                que.append(n)

        return total
