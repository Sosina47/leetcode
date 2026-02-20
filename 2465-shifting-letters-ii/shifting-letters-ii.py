class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = [ord(letter) % 97 for letter in s]
        prefix = [0] * len(s)

        for a, b, c in shifts:
            if c == 0:
                prefix[b] -= 1
                if a > 0: prefix[a - 1] += 1

            else:
                prefix[b] += 1
                if a > 0: prefix[a - 1] -= 1

        diff = 0
        for i in range(len(s) - 1, -1, -1):
            diff += prefix[i]
            s[i] = (s[i] + diff) % 26

        for i in range(len(s)):
            s[i] = chr(s[i] + 97)

        return ''.join(s)
