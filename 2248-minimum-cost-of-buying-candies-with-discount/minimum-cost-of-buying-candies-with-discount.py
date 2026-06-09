class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()

        free = 0
        for i in range(len(cost) - 3, -1, -3):
            free += cost[i]

        return sum(cost) - free