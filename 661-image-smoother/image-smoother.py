class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        image = [[0] * col for _ in range(row)]

        for r in range(row): 
            for c in range(col):
                up = max(0, r - 1)
                down = min(r + 1, row - 1)
                left = max(0, c - 1)
                right = min(c + 1, col - 1)

                total = 0
                for i in range(up, down + 1):
                    for j in range(left, right + 1):
                        total += img[i][j]

                new_row = down - up + 1
                new_col = right - left + 1
                image[r][c] = total // (new_row * new_col)

        return image