class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        next_smaller = defaultdict(lambda : length)
        prev_smaller = defaultdict(lambda : -1)

        stack = []
        for i in range(length):
            while stack and heights[stack[-1]] > heights[i]:
                next_smaller[stack[-1]] = i
                stack.pop()

            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        max_area = 0
        for i in range(length):
            max_area = max(max_area, heights[i] * (next_smaller[i] - prev_smaller[i] - 1))

        return max_area
        
        
        
        
        
        # stack = deque()
        # left = 0
        # max_ = 0

        # for right in range(len(heights)):
        #     if stack and heights[right] >= heights[stack[0]]:

        #         while stack and heights[right] > heights[stack[0]] * (right - left + 1):
        #             if stack[0] == left:
        #                 stack.popleft()

        #                 left += 1
        #                 break
                    
                    
                
                
        #         if heights[right] > heights[stack[0]] * (right - left + 1):
        #             left = right
        #             stack = [right]

        #             max_ = max(max_, heights[right])
        #             # print(right)
        #             continue

        #     while stack and heights[stack[-1]] > heights[right]:
        #         stack.pop()

        #     stack.append(right)

        #     # if len(stack) == 1:
        #     #     left = right

        #     max_ = max(max_, heights[stack[0]] * (right - left + 1))
        #     # print(stack[0], left, max_)

        # return max_
            
