class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3 :
            return False
            

        def solve(a, b, i, count):
            if i == n:
                return count >= 3

            for j in range(i, n):
                if j != i and num[i] == '0':
                    return False

                numm = int(num[i: j + 1])
                if a == -1:
                    if solve(numm, b, j + 1, count + 1):
                        return True

                elif b == -1:
                    if solve(a, numm, j + 1, count + 1):
                        return True

                else:
                    if numm > a + b:
                        return False

                    if numm == a + b:
                        if solve(b, numm, j + 1, count + 1):
                            return True

            return False


        return solve(-1, -1, 0, 0)