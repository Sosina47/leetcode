class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        
        for s in strs:
            ss = [letter for letter in s]
            ss.sort()
            ss = ''.join(ss)
            dict[ss].append(s)

        output = []
        for key in dict:
            output.append(dict[key])

        return output 