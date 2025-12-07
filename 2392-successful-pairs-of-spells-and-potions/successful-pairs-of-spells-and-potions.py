class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        for i in range(len(spells)):
            pot = math.ceil(success / spells[i])
            left = 0
            right = len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= pot:
                    right = mid - 1
                else:
                    left = mid + 1
            
            spells[i] = len(potions) - left
            
        return spells 