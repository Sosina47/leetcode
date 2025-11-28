class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = []
        
        n = len(code)
        if k == 0:
            return [0] * n

        for i in range(n):
            new_num = 0
            index = i

            if k > 0:
                temp_k = 1
                while temp_k <= k:
                    j = (index + temp_k) % n
                    new_num += code[j]
                    temp_k += 1
            else:
                temp_k = -1
                while temp_k >= k:
                    j = (index + temp_k) % n
                    new_num += code[j]
                    temp_k -= 1

            result.append(new_num)
        return result
