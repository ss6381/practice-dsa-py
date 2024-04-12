# In-place palindrome.
# META PHONE SCREEN
# April 2024

# Write a function that returns whether the given string, ignoring punctuation and capitalization, is a palindrome.

# An example of palindrome is:
#   "Race car!"
#   "A man, a plan, a canal, Panama!"
# A palindrome is a chunk of text that is the same backwards and forwards, again, ignoring punctuation and capitalization.

# We are looking for an optimal solution that works in-place.

"""
1. two pointer approach, initialize left and right
2. do simultaneous pass, compare characters, ignore non alphanumeric and make lowercase
"""

class Solution:

    def inplace_palindrome(self, s):
        left = 0
        right = len(s) - 1

        while left <= right:

            while not self.is_alpha(s[left]):
                left += 1
            while not self.is_alpha(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def is_alpha(character):
        """
        checks if the character is a-z A-Z
        returns False if the character is special !$%, as well as numeric 1-9
        """
        pass


if __name__ == '__main__':
    tests = [
        "1ff55", # True
        "1fghf55", # False
        "1fgf55", # True
        "1f55" # True
        "1fg55" # False
        "1Ff55", # True
        "1FghF55", # False
        "1F3,f55..", # True
        ",,1Fgh5.F55", # False
        "444444"
    ]
    s = Solution()
    for test in tests:
        print(s.inplace_palindrome(test))
