class Solution:
    def splitNum(self, num: int) -> int:
        num = list(str(num))
        num.sort()

        num1 = []
        num2 = []

        turn = 0
        for n in num:
            if n == '0':
                continue

            if turn == 0:
                num1.append(n)
            else:
                num2.append(n)
            turn = 1 - turn
        
        num1 = ''.join(num1) if num1 else 0
        num2 = ''.join(num2) if num2 else 0

        return int(num1) + int(num2)