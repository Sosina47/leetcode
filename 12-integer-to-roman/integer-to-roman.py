class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {0: ['V', 'I'], 1: ['L', 'X'], 2: ['D', 'C'], 3: 'M'}
        output = ''

        num = str(num)[::-1]

        for i in range(len(num)):
            n = int(num[i]) - 5

            if n == 4:
                if i == 2:
                    output += dict[i + 1][0] + dict[i][1]
                else:
                    output += dict[i + 1][1] + dict[i][1]
            elif n >= 0:
                for j in range(n):
                    output += dict[i][1]
                output += dict[i][0]
            elif n == -1:
                output += dict[i][0] + dict[i][1]
            else:
                if i == 3:
                    for j in range(n + 5):
                        output += dict[i][0]
                        
                else:
                    for j in range(n + 5):
                        output += dict[i][1]

        return output[::-1]
