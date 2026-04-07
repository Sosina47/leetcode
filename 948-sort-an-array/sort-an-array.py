class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(0, len(nums) - 1, nums)


    def mergeSort(self, left, right, nums):
        if left == right:
            return [nums[left]]

        mid = left + (right - left) // 2

        left_arr = self.mergeSort(left, mid, nums)
        right_arr = self.mergeSort(mid + 1, right, nums)

        return self.merge(left_arr, right_arr)        
        
    def merge(self, left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1

            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

