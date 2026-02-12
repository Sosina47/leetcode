class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])

        new_image = [[0] * col for _ in range(row)]

        for r in range(row): 
            for c in range(col):
                temp_row = max(0, r - 1)
                temp_col = max(0, c - 1)

                total = 0
                count = 0

                for i in range(temp_row, min(r + 1, row - 1) + 1):
                    for j in range(temp_col, min(c + 1, col - 1) + 1):
                        total += img[i][j]
                        count += 1

                new_image[r][c] = total // count

        return new_image
                