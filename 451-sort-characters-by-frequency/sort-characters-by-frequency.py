class Solution:
    def frequencySort(self, s: str) -> str:
        s_freq = Counter(s)
        s_items = list(s_freq.items())

        for i in range(1, len(s_items)):
            j = i - 1
            key = s_items[i]
            while j >= 0:
                if s_items[j][1] < key[1]:
                    s_items[j + 1] = s_items[j]
                    j -= 1
                else: 
                    break
            s_items[j + 1] = key

        output = ''
        for i in range(len(s_items)):
            val = s_items[i][0]
            freq = s_items[i][1]
            while freq > 0:
                output += val
                freq -= 1

        return output