class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy = ['a', 'b', 'c']
        output = []


        def solve(strr):
            if len(strr) == n:
                output.append("".join(strr))
            
                if len(output) == k:
                    return True

                return False

            for i in range(3):
                if not strr or strr[-1] != happy[i]:
                    strr.append(happy[i])

                    if solve(strr):
                        return True

                    strr.pop()

            return False

        solve([])

        return output[k - 1] if k <= len(output) else ""