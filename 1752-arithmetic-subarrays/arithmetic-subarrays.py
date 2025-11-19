class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        length = len(l)
        output = [True] * length
        for i in range(length):
            temp = nums[l[i]: r[i] + 1]
            temp.sort()
            for j in range(1, len(temp) - 1):
                if temp[j] - temp[j - 1] != temp[j + 1] - temp[j]:
                    output[i] = False
                
            
        return output