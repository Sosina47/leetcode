# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         nums_counter = Counter(nums)
#         output = []
#         for i in nums_counter:
#             if nums_counter[i] > len(nums) // 3:
#                 output.append(i)

#         return output

































class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lst = Counter(nums)
        n = len(nums)
        output = []
        
        for key in lst:
            if lst[key] > n//3:
                output.append(key)

        return output