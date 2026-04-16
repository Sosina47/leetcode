class Solution:
    def smallestNumber(self, pattern: str) -> str:
        seen = set()
        output = []
        n = len(pattern)

        def solve(path):
            if len(path) == n + 1:
                return ''.join(map(str, path))

            for i in range(1, 10): 
                if not path:
                    path.append(i)
                    seen.add(i)

                    output = solve(path)

                    if output:
                        return output
                        
                    seen.remove(path.pop())

                else:
                    if i in seen:
                        continue

                    index = len(path) - 1

                    if pattern[index] == 'I':
                        if path[-1] < i:
                            path.append(i)
                            seen.add(i)

                            output = solve(path)

                            if output:
                                return output

                            seen.remove(path.pop())

                    else:
                        if path[-1] > i:
                            path.append(i)
                            seen.add(i) 

                            output = solve(path)
                            if output:
                                return output

                            seen.remove(path.pop())
                
            return ''

                
        return solve([])
