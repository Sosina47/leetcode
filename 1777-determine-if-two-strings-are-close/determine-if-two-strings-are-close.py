class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        if count1.keys() != count2.keys():
            return False

        for key in count1:
            k = ''
            for key2 in count2:
                if count1[key] == count2[key2]:
                    k = key2
                    break
            if not k:
                return False

            del count2[k]

        return True