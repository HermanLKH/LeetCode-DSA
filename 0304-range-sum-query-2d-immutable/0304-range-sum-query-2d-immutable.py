class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.prefix = [[0] * (len(matrix[0]) + 1)]

        for row_i, row in enumerate(matrix):
            prefix_row = [0]

            for i, num in enumerate(row):
                prefix = num + self.prefix[row_i][i + 1] + prefix_row[i] - self.prefix[row_i][i]
                prefix_row.append(prefix)

            self.prefix.append(prefix_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.prefix[row1][col1]
        b = self.prefix[row1][col2 + 1]
        c = self.prefix[row2 + 1][col1]
        d = self.prefix[row2 + 1][col2 + 1]

        return d - b - c + a


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)