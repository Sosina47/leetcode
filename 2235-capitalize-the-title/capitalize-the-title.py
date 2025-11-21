class Solution:
    def capitalizeTitle(self, title: str) -> str:
        titleList = [word.capitalize() for word in title.split()]
        print(titleList)
        
        for i in range(len(titleList)):
            if len(titleList[i]) <= 2:
                titleList[i] = titleList[i].lower()
        return ' '.join(titleList)