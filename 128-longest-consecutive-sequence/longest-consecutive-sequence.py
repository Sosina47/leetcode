class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        count = max_count = 0
        seen = {}

        for i in range(len(nums)):
            temp = nums[i]
            num = nums[i]

            while True:
                if num in seen:
                    count += seen[num]
                    break
                
                if num not in nums_set:
                    break

                count += 1
                num += 1

            max_count = max(max_count, count)

            while temp in nums_set and temp not in seen:
                seen[temp] = count
                temp += 1
                count -= 1
            
            max_count = max(max_count, count)
            count = 0

        return max_count