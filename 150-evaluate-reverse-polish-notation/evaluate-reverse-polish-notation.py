class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+': '+', '-': '-', '*': '*', '/': '//'}

        stack = []
        for i in range(len(tokens)):
            if tokens[i] in operators:
                b = stack.pop()
                a = stack.pop()

                if tokens[i] == '/':
                    stack.append(int(a / b))
                else:
                    stack.append(eval(f'{a} {operators[tokens[i]]} {b}'))
            
            else:
                stack.append(int(tokens[i]))
            
        return stack[0]