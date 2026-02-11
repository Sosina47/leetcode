class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        frequency = Counter(nums)

        num = 0
        val = 0

        for key in frequency:
            if frequency[key] > val:
                val = frequency[key]
                num = key
        
        length = len(nums)
        curr = 0

        for i in range(length):
            if nums[i] == num:
                curr += 1
                val -= 1
            
            if (i + 1) / 2 < curr and (length - i - 1) / 2 < val and i < length - 1:
                return i

        return -1