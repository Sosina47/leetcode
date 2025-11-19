class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            temp = []
            for col in range(i + 1):
                if col == 0 or col == i:
                    temp.append(1)
                else:
                    temp.append(output[-1][col - 1] + output[-1][col])
            output.append(temp)

        return output
    