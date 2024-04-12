"""
Snap - 1st Round
Given a string that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

input: "()"
output: "()"

1 --> 0 --> -1
input: "(a))"
output: "(a)"

1 --> 2 --> 1
3
input: "((a)"
output: "(a)"

-1 --> 0
input: ")("
output: ""

input: "()))"
output: "()"

input: "()(()"
output: "()()"

input: "(a))()"
output: "(a)()"

3

// stack, when we see an ( , we push )
// when we see ) , pop off the stack to compare

// keep two counters for open and closed parentheses
// check the difference,
//. if it is greater than 0, remove open parenthesis
//. if it is less than 0, remove closed parenthesis

"""

class Solution:
    
	def remove_invalid_parenthesis(self):
		pass

if __name__ == '__main__':
	s = Solution()
	print(s.remove_invalid_parenthesis())