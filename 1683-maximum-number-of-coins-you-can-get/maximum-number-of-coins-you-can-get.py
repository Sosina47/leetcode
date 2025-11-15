class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        length = len(piles)
        max_coin = 0
        i = 1
        while i < (length - (length // 3)):
            max_coin += piles[i] 
            i += 2

        return max_coin