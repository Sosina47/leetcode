class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        output = []

        hash = {
            '2' : ('a', 'b', 'c'), 
            '3' : ('d', 'e', 'f'), 
            '4' : ('g', 'h', 'i'), 
            '5' : ('j', 'k', 'l'), 
            '6' : ('m', 'n', 'o'), 
            '7' : ('p', 'q', 'r', 's'), 
            '8' : ('t', 'u', 'v'), 
            '9' : ('w', 'x', 'y', 'z')
        }

        def dfs(start, path):
            if len(path) == length:
                output.append("".join(path))
                return 

            for i in range(start, length):
                for ch in hash[digits[i]]:
                    path.append(ch)

                    dfs(i + 1, path)
                    path.pop()

        dfs(0, [])
        return output 