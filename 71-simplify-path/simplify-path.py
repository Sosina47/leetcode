class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = [way for way in path.split('/')]
        output = []
        for i in range(len(pathList)):
            if pathList[i] == '..':
                if output:
                    output.pop()
            elif pathList[i] != '.' and pathList[i] != '':
                output.append(pathList[i])

        if not output:
            return '/'
        simplified = []
        for way in output:
            simplified.append('/')
            simplified.append(way)

        return ''.join(simplified)