class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy = ['a', 'b', 'c']
        output = []


        def solve(strr):
            if len(strr) == n:
                output.append("".join(strr))
                return 

            for i in range(3):
                if not strr or strr[-1] != happy[i]:
                    strr.append(happy[i])

                    solve(strr)

                    strr.pop()

        solve([])
        
        return output[k - 1] if k <= len(output) else ""