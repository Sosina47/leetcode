class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordDict = set(wordDict)

        maxx = 0
        for word in wordDict:
            maxx = max(maxx, len(word))

        output = []

        def dfs(i, j, path):
            if i == j == n: 
                output.append(" ".join(path))
                return 
            
            while j < n: 
                if j - i + 1 > maxx: 
                    return                
                
                if s[i: j + 1] in wordDict: 
                    path.append(s[i: j + 1])
                    
                    dfs(j + 1, j + 1, path)
                    path.pop()

                j += 1
                    
                    
        dfs(0, 0, [])

        return output