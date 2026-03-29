class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse = True)
        length = len(nums)
        subsets = [0] * k

        each = sum(nums) / k
        found = False

        def solve(index, subsets):
            nonlocal found
            
            if index == length:
                if max(subsets) == min(subsets) == each:
                    found = True
                return 

            for i in range(k):
                if i > 0 and subsets[i] == subsets[i - 1]:  
                    continue

                subsets[i] += nums[index]
                
                if subsets[i] <= each:
                    solve(index + 1, subsets)

                subsets[i] -= nums[index]

                if found:
                    return True

                if subsets[i] == 0:
                    break

        return True if solve(0, subsets) else False
