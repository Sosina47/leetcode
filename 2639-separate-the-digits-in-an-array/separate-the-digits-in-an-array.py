class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []
        for i in map(str, nums):
            for j in i:
                output.append(int(j))

        return output