class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i + 1 for i in range(n)]

        k_ = k 
        i = 0

        while len(players) > 1 and i < len(players):
            k_ -= 1
            if k_ == 0:
                players.pop(i)
                i -= 1
                k_ = k
            
            i += 1
            i %= len(players) 
            
        return players[0]