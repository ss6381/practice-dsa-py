
class Solution:
	def is_valid_parenthesis(self, s):
		stack = []
		for c in s:
			if c == '(':
				stack.append(')')
			elif c == '{':
				stack.append('}')
			elif c == '[':
				stack.append(']')
			elif len(stack) == 0 or stack.pop() != c:
				return False
		return len(stack) == 0

if __name__ == '__main__':
	s = Solution()
	tests = [
		'()', # True
		'()[]{}', # True
		'(]', # False
		'([)]', # False
		'{[]}', # True
		'[[(]])', # False
	]
	for test in tests:
		print(s.is_valid_parenthesis(test))