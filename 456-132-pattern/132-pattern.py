class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        k = float('-inf')
        stack = [] # decreasing 

        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] < nums[i]:
                num = stack.pop()
                k = max(k, num)
            
            if nums[i] < k: # checks if the current num is smaller than k
                return True 
                
            stack.append(nums[i])

        return False
