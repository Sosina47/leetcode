from collections import Counter
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        seen = {chars[0]: 1}
        output = []

        for i in range(1, len(chars)):
            if chars[i] not in seen:
                key = list(seen.keys())
                output.append(key[0])

                if seen[chars[i - 1]] > 1:
                    ch = seen[chars[i - 1]]
                    vals = []
                    while ch > 0:
                        val = ch % 10
                        ch //= 10
                        vals.append(str(val))

                    vals.reverse()
                    output.extend(vals)
                
                seen = {chars[i]: 1}
            else:
                seen[chars[i]] += 1

        key = list(seen.keys())
        output.append(key[0])
        
        if seen[key[0]] > 1:
            ch = seen[chars[i - 1]]
            vals = []
            while ch > 0:
                val = ch % 10
                ch //= 10
                vals.append(str(val))

            vals.reverse()
            output.extend(vals)

        n = len(output)
        for i in range(n):
            chars[i] = output[i]
        
        return n