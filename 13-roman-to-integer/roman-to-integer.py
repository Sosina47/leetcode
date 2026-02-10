class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        output = [symbols[s[0]]]
        for i in range(1, len(s)):
            if symbols[s[i]] > symbols[s[i - 1]]:
                output[-1] = symbols[s[i]] - output[-1]
            
            elif s[i] == s[i - 1]:
                output[-1] += symbols[s[i]]
            
            else:
                output.append(symbols[s[i]])

        return sum(output)

            




            # if symbols[s[i]] == 5 or symbols[s[i]] == 50 or symbols[s[i]]== 500

            # if s[i] == s[i - 1]:
            #     output += symbols[s[i]]

            # else:
            #     output *= 10
            #     output += symbols[s[i]]
        
        return output
