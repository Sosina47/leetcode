class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k - 1

        output = []
        while right < len(nums): 
            mid = left
            while mid < right: 
                if nums[mid] + 1 != nums[mid + 1]:
                    output.append(-1)
                    break
                mid += 1
            else:
                output.append(nums[right])
            
            left += 1 
            right += 1
        
        return output 