class Solution:
    def capitalizeTitle(self, title: str) -> str:
        titleList = []
        
        for word in title.split():
            if len(word) > 2:
                titleList.append(word.capitalize())
            else:
                titleList.append(word.lower())

        return ' '.join(titleList)