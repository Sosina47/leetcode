class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        str_list = [letter for letter in word]
        index = str_list.index(ch)
        i, j = 0, index 
        while i < j:
            str_list[i], str_list[j] = str_list[j], str_list[i]
            i += 1
            j -= 1

        return ''.join(str_list)
    