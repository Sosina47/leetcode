class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        operation = {'+', '-', '*', '/'}
        stack = []

        
        for i in range(len(tokens)):
            result = 0
            if tokens[i] in operation:
                if tokens[i] == '/':
                    if int(stack[-1]) < 0 or int(stack[-2]) < 0:
                        result += eval(f'int({stack[-2]} {tokens[i]} {stack[-1]})')
                    else:
                        tokens[i] = '//'
                        result += eval(f'int({stack[-2]} {tokens[i]} {stack[-1]})')
                else: 
                    result += eval(f'{stack[-2]} {tokens[i]} {stack[-1]}')
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(tokens[i])
            
        return result
    
