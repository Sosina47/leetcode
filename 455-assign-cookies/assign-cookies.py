class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        count_content = 0

        j = 0
        for i in range(len(g)):
            while j < len(s):
                if g[i] <= s[j]:
                    count_content += 1
                    j += 1
                break

        return count_content
