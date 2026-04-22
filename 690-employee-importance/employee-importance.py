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

        for i in employees:
            adj_list[i.id].append(i.importance)
            adj_list[i.id].append(i.subordinates)


        def dfs(idx):
            count = adj_list[idx][0]

            for val in adj_list[idx][1]:
                count += dfs(val)

            return count            
            

        return dfs(id)