class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        typed_s = []
        for letter in s:
            if letter == '#':
                if typed_s:
                    typed_s.pop()
            else:
                typed_s.append(letter)
                
        typed_t = []
        for letter in t:
            if letter == '#':
                if typed_t:
                    typed_t.pop()
            else:
                typed_t.append(letter)

        return typed_s == typed_t