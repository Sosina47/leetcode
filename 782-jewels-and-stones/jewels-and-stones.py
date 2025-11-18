class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in range(len(jewels)):
            count += stones.count(jewels[i])
        return count
    