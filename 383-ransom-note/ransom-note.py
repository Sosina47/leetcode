class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_r = Counter(ransomNote)
        count_m = Counter(magazine)

        for key in count_r:
            if key not in count_m or count_r[key] > count_m[key]:
                return False

        return True