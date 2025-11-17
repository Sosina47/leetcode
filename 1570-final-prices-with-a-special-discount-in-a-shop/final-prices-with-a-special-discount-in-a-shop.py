class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = []
        for i in range(len(prices)):
            foundDiscount = False
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    output.append(prices[i] - prices[j])
                    foundDiscount = True
                    break
            if not foundDiscount:
                output.append(prices[i])
        
        return output
    