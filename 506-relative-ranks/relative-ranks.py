class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        newNum = score.copy()
        newNum.sort(reverse=True)
        rank = {}
        for i in range(len(newNum)):
            if i == 0:
                rank[newNum[i]] = 'Gold Medal'
            elif i == 1:
                rank[newNum[i]] = 'Silver Medal'
            elif i == 2:
                rank[newNum[i]] = 'Bronze Medal'
            else:
                rank[newNum[i]] = str(i + 1)
                
        for i in range(len(score)):
            score[i] = rank[score[i]]
            
        return score