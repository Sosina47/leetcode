class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = []
        file_paths = []

        file_dict = defaultdict(list)
        
        for i in range(len(paths)):
            files = paths[i].split()

            for j in range(1, len(files)):
                idx = files[j].find('(')
                idx1 = idx + 1

                new_content = ''
                while files[j][idx1] != ')':
                    new_content += files[j][idx1]
                    idx1 += 1

                contents.append(new_content)
                file_paths.append('/'.join([files[0], files[j][:idx]]))

        for i in range(len(contents)):
            file_dict[contents[i]].append(file_paths[i])

        output = []
        for val in file_dict.values():
            if len(val) >= 2:
                output.append(val)

        return output