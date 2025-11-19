class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = []
        for i in range(len(boxes)):
            moves = 0
            for j in range(len(boxes)):
                if i != j:
                    if boxes[j] == '1':
                        moves += abs(j - i)
            output.append(moves)

        return output