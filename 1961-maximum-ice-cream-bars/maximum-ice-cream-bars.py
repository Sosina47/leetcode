class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        costs = list(accumulate(costs))

        return bisect_right(costs, coins)