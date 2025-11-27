class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        smallest = prices[0]
        for i in range(1, len(prices)):            
            max_profit = max(max_profit, prices[i] - smallest)

            smallest = min(smallest, prices[i])

        return max_profit
    