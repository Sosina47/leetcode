class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ''
        word = strs[0]
        for i in range(len(word)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or word[i] != strs[j][i]:
                    return longest
                
            longest += word[i]
        
        return longest
