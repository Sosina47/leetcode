class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        
        return [c for c, n in nums_count.items() if n == 1]