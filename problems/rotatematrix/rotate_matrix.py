from typing import List


# time complexity: O(N)
# space complexity: O(1)
def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while left < right and top < bottom:
        curr = matrix[top + 1][left]

        for i in range(left, right + 1):
            curr, matrix[top][i] = matrix[top][i], curr
        top += 1

        for i in range(top, bottom + 1):
            curr, matrix[i][right] = matrix[i][right], curr
        right -= 1

        for i in range(right, left - 1, -1):
            curr, matrix[bottom][i] = matrix[bottom][i], curr
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            curr, matrix[i][left] = matrix[i][left], curr
        left += 1

    return matrix


if __name__ == "__main__":
    tests = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [])(
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]], []
        ),
        ([[1]], []),
        ([[1, 2], [3, 4]], []),
    ]
    for matrix in tests:
        print(rotate_matrix(matrix))
