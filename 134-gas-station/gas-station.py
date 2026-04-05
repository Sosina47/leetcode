class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        start = 0

        for i in range(2 * n):
            if cost[i % n] <= tank + gas[i % n]:
                tank += gas[i % n] - cost[i % n]
            
            else:
                start = i + 1
                tank = 0

            if i - start + 1 == n:
                return start

        return -1