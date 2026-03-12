class Solution:
    def minOperations(self, nums: List[int]) -> int:
        queue = deque()
        min_op = 0

        i = 0
        while i < len(nums):
            while len(queue) < 3 and i < len(nums):
                queue.append(nums[i])
                i += 1

            if len(queue) < 3:
                if 0 in queue:
                    return -1
                else:
                    return min_op
            
            if queue[0] == 1:
                queue.popleft()
            
            else:
                for j in range(3):
                    queue[j] = 1 - queue[j]  
                
                min_op += 1
                queue.popleft()
        
        if 0 in queue:
            return -1
        else:
            return min_op

        