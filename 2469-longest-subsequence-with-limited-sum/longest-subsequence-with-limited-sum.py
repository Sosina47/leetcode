class Solution():
    def merge(self, nums, low, mid, high):
        left = low
        right = mid + 1

        result = []
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                result.append(nums[left])
                left += 1
            else:
                result.append(nums[right])
                right += 1

        while left <= mid:
            result.append(nums[left])
            left += 1

        while right <= high:
            result.append(nums[right])
            right += 1

        for index in range(len(result)):
            nums[low + index] = result[index]
            
            
    def merge_sort(self, nums, low, high):
        if low == high:
            return 

        mid = (low + high) // 2
        self.merge_sort(nums, low, mid)  
        self.merge_sort(nums, mid + 1, high)

        self.merge(nums, low, mid, high)
    
    def answerQueries(self, nums: List[int], queries: List[int]):
        self.merge_sort(nums, 0, len(nums) - 1)
        
        length = len(nums)
        for index in range(1, length):
            nums[index] += nums[index - 1]
            
        def bin_search(nums, q):
            left = 0
            right = len(nums)
            
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= q:
                    left = mid + 1
                else:
                    right = mid
                    
            return left
        
        result = []
        for q in queries:
            result.append(bin_search(nums, q))
        
        return result