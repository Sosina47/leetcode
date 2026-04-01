class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = set()
        n = len(nums)
        nums.sort()

        for i in range(n - 2):            
            j = i + 1
            k = n - 1

            while j < k:
                summ = nums[j] + nums[k] 

                if nums[i] + summ == 0:
                    output.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k  -= 1
                
                elif nums[i] + summ > 0:
                    k -= 1
                
                else:
                    j += 1

        return list(output) 