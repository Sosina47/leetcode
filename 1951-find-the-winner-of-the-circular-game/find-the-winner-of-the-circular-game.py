class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i + 1 for i in range(n)]
        index = 0
        while len(players) > 1:
            index = (index + k - 1) % len(players)
            players.pop(index)
        
        return players[0]