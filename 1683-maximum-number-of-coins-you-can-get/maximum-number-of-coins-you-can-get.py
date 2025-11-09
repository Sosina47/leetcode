class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        max_coins = 0
        i = 1
        length = len(piles)
        while i < length - (length // 3):
            max_coins += piles[i]
            i += 2
        
        return max_coins