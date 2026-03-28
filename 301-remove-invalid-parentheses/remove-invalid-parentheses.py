class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        length = len(s)
        output = set()
        max_length = 0
        open = close = 0

        for i in range(length):
            if s[i] == '(':
                open += 1

            elif s[i] == ')':
                if open > close:
                    close += 1
                    max_length += 2
            
            else:
                max_length += 1

        if max_length == 0:
            return [""]

            

        def solve(start, open, close, path):
            nonlocal max_length
            
            if close > open:
                return

            if len(path) > max_length: 
                return 
            
            if start == length:
                if close == open and len(path) == max_length:
                    output.add("".join(path))
                return 
            
            if s[start] == '(':
                open += 1

            elif s[start] == ')':
                close += 1

            path.append(s[start])
            solve(start + 1, open, close, path)
            path.pop()

            if s[start] == '(':
                open -= 1
            elif s[start] == ')':
                close -= 1

            if s[start] in "()":
                solve(start + 1, open, close, path)



        solve(0, 0, 0, [])
        
        return list(output)
