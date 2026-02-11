

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        changed.sort()

        output = []
        seen = 0
        length = len(changed)

        for i in range(length):
            if changed[i] not in count:
                continue

            if count[changed[i]] == 1:
                del count[changed[i]]
            else:
                count[changed[i]] -= 1


            n = changed[i] / 2
            if n in count:
                output.append(int(n))

                if count[n] == 1:
                    del count[n]
                else:
                    count[n] -= 1

                seen += 2
                continue

            n = changed[i] * 2
            if n in count:
                output.append(changed[i])
                
                if count[n] == 1:
                    del count[n]
                else:
                    count[n] -= 1

                seen += 2

        if seen < length:
            return []
        
        return output

