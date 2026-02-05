from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        block_comment = False
        temp = ''

        for i in range(len(source)):
            line = source[i] 
            right = 0

            while right < len(line):
                if line[right: right + 2] == '/*' and not block_comment:
                    block_comment = True
                    right += 1

                elif line[right: right + 2] == '*/' and block_comment: 
                    block_comment = False
                    right += 1

                elif line[right: right + 2] == '//' and not block_comment:
                    break

                elif not block_comment:
                    temp += line[right]

                right += 1

            if not block_comment and temp != '':
                result.append(temp)
                temp = ''

        return result