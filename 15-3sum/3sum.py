class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        print(nums)

        output = []
        
        for i in range(n - 2):            
            seen = set()

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # print(i, nums[i])

            j = i + 1
            k = n - 1

            while j < k:
                if nums[j] in seen:
                    j += 1
                    continue

                summ = nums[j] + nums[k] 

                if nums[i] + summ == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    seen.add(nums[j])

                    j += 1
                    k  -= 1
                
                elif nums[i] + summ > 0:
                    k -= 1
                
                else:
                    seen.add(nums[j])
                    j += 1

        return output