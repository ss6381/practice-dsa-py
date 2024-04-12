
class Solution:

    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.
    Note: The solution set must not contain duplicate triplets.

    Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],
    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

    Time complexity: O(N^2)
    Space complexity: O(1)

    SOLUTION:
    1. Sort the array.
    2. Iterate through the array.
    3. For each element, use two pointers to find the other two elements.
    4. Skip duplicates.
    5. If the sum is less than 0, increment left pointer.
    6. If the sum is greater than 0, decrement right pointer.
    7. If the sum is 0, add the triplet to the result.
    8. Skip duplicates.
    9. Increment left pointer.
    10. Decrement right pointer.
    11. Return the result.
    """
    def three_sum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
    
if __name__ == '__main__':
    s = Solution()
    tests = [
        [-1, 0, 1, 2, -1, -4],
        [],
        [0],
    ]
    for test in tests:
        print(s.three_sum(test))
