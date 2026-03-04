class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            prefix[start] += (2 * direction - 1)
            prefix[end + 1] -= (2 * direction - 1)

        prefix = list(itertools.accumulate(prefix))
        for i in range(len(s)):
            prefix[i] += ord(s[i]) - ord('a')
            prefix[i] %= 26
            prefix[i] = chr(prefix[i] + ord('a'))

        prefix.pop()
        return ''.join(prefix) 