class Solution:
    def isValid(self, s: str) -> bool:
        open_symbol = {0: '(', 1: '[', 2: '{'}
        close_symbol = {')': 0, ']': 1, '}': 2}

        opened = []
        
        for index in range(len(s)):
            symbol = s[index]
            if symbol in open_symbol.values():
                opened.append(symbol)
            if symbol in close_symbol:
                if not opened:
                    return False
                if opened[-1] == open_symbol[close_symbol[symbol]]:
                    opened.pop()
                else:
                    return False
        return not opened