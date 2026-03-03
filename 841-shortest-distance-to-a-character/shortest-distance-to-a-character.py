class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pos = [i for i in range(len(s)) if s[i] == c]
        right = 0
        output = []

        for i in range(len(s)):
            if right == 0:
                if pos[right] <= i:
                    output.append(i - pos[right])
                else:
                    output.append(pos[right] - i)
            else:
                if pos[right] >= i >= pos[right - 1]:
                    output.append(min(pos[right] - i, i -pos[right - 1]))
                else:
                    output.append(i - pos[right])
            
            if i == pos[right]:
                right = right + 1 if right + 1 < len(pos) else right

        return output 