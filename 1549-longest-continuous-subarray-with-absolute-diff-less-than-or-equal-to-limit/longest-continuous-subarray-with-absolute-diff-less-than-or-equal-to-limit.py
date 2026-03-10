class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()
        max_length = 0
        left = 0

        for right in range(len(nums)):
            while increasing and increasing[-1] > nums[right]:
                increasing.pop()
            
            increasing.append(nums[right])

            while decreasing and decreasing[-1] < nums[right]:
                decreasing.pop()

            decreasing.append(nums[right])

            while decreasing[0] - increasing[0] > limit:
                if decreasing[0] == nums[left]:
                    decreasing.popleft()

                elif increasing[0] == nums[left]:
                    increasing.popleft()

                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length