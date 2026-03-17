class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        # whenever we have +2 operation we have -2 operation so the only thing we gotta do is find how many +2 or -2 operations we are required to do

        nums.sort()
        nums_even = [num for num in nums if num % 2 == 0]
        nums_odd = [num for num in nums if num % 2 == 1]

        target.sort()
        target_even = [num for num in target if num % 2 == 0]
        target_odd = [num for num in target if num % 2 == 1]      

        # diff = []
        operations = 0
        for i in range(len(nums_even)):
            # diff.append(abs(nums_even[i] - target_even[i]) // 2)
            diff_ = target_even[i] - nums_even[i]
            if diff_ > 0:
                operations += diff_ // 2
        
        for i in range(len(nums_odd)):
            # diff.append(abs(nums_odd[i] - target_odd[i]) // 2)
            diff_ = target_odd[i] - nums_odd[i]
            if diff_ > 0:
                operations += diff_ // 2

        return operations
        
        # diff.sort(reverse = True)
        # operations = diff[0] if diff else  0
        # cur_op = diff[0] if diff else  0

        # return sum(diff) // 2 
        # print(diff)

        # for d in diff[1:]:
        #     if cur_op >= d:
        #         cur_op -= d
        #     else:
        #         operations += d - cur_op
        #         cur_op = d - cur_op
                
        # return operations 