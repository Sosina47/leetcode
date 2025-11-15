class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []
        for i in range(len(operations)):
            val = operations[i]
            if val == '+':
                output.append(int(output[-1]) + int(output[-2]))
            elif val == 'D':
                output.append(int(output[-1]) * 2)
            elif val == 'C':
                output.pop()
            else:
                output.append(int(val))

        return sum(output)