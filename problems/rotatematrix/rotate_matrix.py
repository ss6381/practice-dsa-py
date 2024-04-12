
class Solution:
    
	# time complexity: O(N)
	# space complexity: O(1)
	def rotate_matrix(self, matrix):
		top = 0
		bottom = len(matrix) - 1
		left = 0
		right = len(matrix[0]) - 1

		while left < right and top < bottom:
			curr = matrix[top+1][left]

			for i in range(left, right+1):
				curr, matrix[top][i] = matrix[top][i], curr
			top += 1

			for i in range(top, bottom+1):
				curr, matrix[i][right] = matrix[i][right], curr
			right -= 1

			for i in range(right, left-1, -1):
				curr, matrix[bottom][i] = matrix[bottom][i], curr
			bottom -= 1

			for i in range(bottom, top-1, -1):
				curr, matrix[i][left] = matrix[i][left], curr
			left += 1

		return matrix
	
if __name__ == '__main__':
	tests = [
		[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
		[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
		[[1]],
		[[1, 2], [3, 4]],
	]
	for matrix in tests:
		s = Solution()
		print(s.rotate_matrix(matrix))

# func RotateMatrix(mat [][]int) [][]int {
# 	top := 0
# 	bottom := len(mat) - 1
# 	left := 0
# 	right := len(mat[0]) - 1

# 	for left < right && top < bottom {
# 		curr := mat[top+1][left]

# 		for i := left; i <= right; i++ {
# 			curr, mat[top][i] = mat[top][i], curr
# 		}
# 		top++

# 		for i := top; i <= bottom; i++ {
# 			curr, mat[i][right] = mat[i][right], curr
# 		}
# 		right--

# 		for i := right; i >= left; i-- {
# 			curr, mat[bottom][i] = mat[bottom][i], curr
# 		}
# 		bottom--

# 		for i := bottom; i >= top; i-- {
# 			curr, mat[i][left] = mat[i][left], curr
# 		}
# 		left++
# 	}

# 	return mat
# }
