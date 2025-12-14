class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odds = math.ceil((high - low) / 2)
        if high % 2 and low % 2:
            return odds + 1
        
        return odds