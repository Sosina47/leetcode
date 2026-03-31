class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def findIndex(num):
            left = 0
            right = n - 1

            while right >= left:
                mid = (right + left) // 2

                if nums[mid] >= num:
                    right = mid - 1
                
                else:
                    left = mid + 1

            return left 

        first = findIndex(target) 
        last = findIndex(target + 1) - 1

        if first < 0 or first >= n or nums[first] != target:
            first = -1
            
        if last < 0 or last >= n or nums[last] != target:
            last = -1

        return [first, last]
        