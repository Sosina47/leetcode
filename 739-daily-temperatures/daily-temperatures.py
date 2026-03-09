class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        answer = [0] * length 
        
        stack = []
        for i in range(length):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                t = stack.pop()
                answer[t] = i - t

            else:
                stack.append(i)

        return answer 