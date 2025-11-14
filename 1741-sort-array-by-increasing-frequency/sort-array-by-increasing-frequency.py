class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        i = 1
        while i < len(nums):
            j = i - 1
            key = nums[i]
            while j >= 0 and nums_count[nums[j]] > nums_count[key]:
                nums[j + 1] = nums[j]
                j -= 1
            while j >= 0 and nums_count[nums[j]] == nums_count[key]:
                if nums[j] < key:
                    nums[j + 1] = nums[j]
                    j -= 1
                else:
                    break
                
                print(nums[j], key)
            i += 1
            nums[j + 1] = key
        
        return nums
    