class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: abs(x))

        num = nums[-1] * nums[-2]
        return max(num * 100000, num * -100000)
        
