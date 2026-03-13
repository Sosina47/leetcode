class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                odds += 1
        
        return min(odds, len(position) - odds)