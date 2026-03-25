# if we initially have a range [1, x] that can cover upto M and if we add y (1 <= y <= x + 1) to the range, then we will have an extended maximum upto M + y. (we can cover upto M + y)


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count_patches = 0
        max_range = 0

        for i in range(len(nums)):

            # check if the current number is out of range
            while nums[i] > max_range + 1: 
                
                if max_range >= n:
                    return count_patches

                count_patches += 1

                # add the minimun number that's out of range
                max_range += (max_range + 1)

            max_range += nums[i] # our new max_range is extended to max_range + nums[i]

        while max_range < n:
            max_range += (max_range + 1)
            count_patches += 1

        return count_patches