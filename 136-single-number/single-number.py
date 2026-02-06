class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lst = Counter(nums)
        for key, val in lst.items():
            if val == 1: 
                return key

