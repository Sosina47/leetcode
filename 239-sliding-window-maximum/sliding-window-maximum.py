class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonically decreasing queue
        answer = []
        queue = deque()
        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)
        answer.append(nums[queue[0]])
        
        for i in range(k, len(nums)):
            if i - queue[0] == k:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)
            answer.append(nums[queue[0]])

        return answer 