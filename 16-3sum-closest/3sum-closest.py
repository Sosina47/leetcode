class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        minn = float("inf")

        for i in range(len(nums)):
            j = i + 1
            k = n - 1

            while j < k: 
                total = nums[i] + nums[j] + nums[k]
                
                if abs(total - target) < abs(minn - target): 
                    minn = total


                if target == total: 
                    return total

                if total > target: 
                    k -= 1

                else: 
                    j += 1

        return minn

            