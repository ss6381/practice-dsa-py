class TestCase:
	def __init__(self, arr, target, expected):
		self.arr = arr
		self.target = target
		self.expected = expected

class Solution:
    
	def binary_search(self, arr, target):
		if not arr:
			return -1
		left, right = 0, len(arr) - 1
		while left <= right:
			mid = (left + right) // 2
			if arr[mid] == target:
				return mid
			if arr[mid] > target:
				right = mid - 1
			else:
				left = mid + 1
		return -1

if __name__ == '__main__':
	s = Solution()

	test_cases = [
		TestCase(
			arr=[1, 5, 7, 12, 24, 26, 46, 75, 103, 125, 235],
			target=235,
			expected=10
		),
		TestCase(
			arr=[1, 5, 7, 12, 24, 26, 46, 75, 103, 125, 235],
			target=7,
			expected=2
		),
		TestCase(
			arr=[1, 5, 7, 12, 24, 26, 46, 75, 103, 125, 235],
			target=9,
			expected=-1
		)
	]

	for i, test in enumerate(test_cases):
		actual = s.binary_search(test.arr, test.target)
		if actual == test.expected:
			print(f"Test {i+1} succeeded!")
		else:
			print(f"Failed, expected {test.expected} but got {actual}")