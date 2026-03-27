class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def playing(i, j):
            if i == j:
                return nums[i]
            
            return max(nums[i] - playing(i + 1, j), nums[j] - playing(i, j - 1))

        
        output = []
        output = playing(0, len(nums) - 1)
        
        return output >= 0
        
        
