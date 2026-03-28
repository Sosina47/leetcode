class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def back(i, path):
            if len(path) == length:
                output.append("".join(path))
                return

            if s[i].isalpha():
                path.append(s[i])
                back(i + 1, path)

                path.pop()

                ch = s[i].swapcase()
                path.append(ch)

                back(i + 1, path)
                path.pop()

            else:
                path.append(s[i])
                back(i + 1, path)

                path.pop()

        output = []
        length = len(s)

        back(0, []) 
        return output
