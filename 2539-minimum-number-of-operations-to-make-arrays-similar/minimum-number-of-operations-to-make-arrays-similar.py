class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        nums_even = [num for num in nums if num % 2 == 0]
        nums_odd = [num for num in nums if num % 2 == 1]

        target.sort()
        target_even = [num for num in target if num % 2 == 0]
        target_odd = [num for num in target if num % 2 == 1]      

        diff = []
        for i in range(len(nums_even)):
            diff.append(abs(nums_even[i] - target_even[i]) // 2)
        
        for i in range(len(nums_odd)):
            diff.append(abs(nums_odd[i] - target_odd[i]) // 2)
        
        diff.sort(reverse = True)
        operations = diff[0] if diff else  0
        cur_op = diff[0] if diff else  0

        return sum(diff) // 2 

        for d in diff[1:]:
            if cur_op >= d:
                cur_op -= d
            else:
                operations += d - cur_op
                cur_op = d - cur_op
                
        return operations 