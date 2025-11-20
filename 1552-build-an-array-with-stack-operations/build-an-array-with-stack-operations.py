class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        stream = [i for i in range(1, n + 1)]
        stack = []

        if not stack:
                stack.append(stream[0])
                operations.append('Push')
        i = 0
        j = 1
        while i < len(target) and stack != target:            
            if stack[-1] != target[i]:
                stack.pop()
                operations.append('Pop')
            else:
                 i += 1
            
            stack.append(stream[j])
            operations.append('Push')
            j += 1
            
        print(stack)
        return operations