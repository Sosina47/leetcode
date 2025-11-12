class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = [word for word in s.split()]
        for i in range(len(s_list)):
            temp = [letter for letter in s_list[i]]
            left, right = 0, len(temp) - 1

            while left < right:
                temp[left], temp[right] = temp[right], temp[left]
                left += 1
                right -= 1
            s_list[i] = ''.join(temp)
        
        return ' '.join(s_list)