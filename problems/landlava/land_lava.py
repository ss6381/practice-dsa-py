# Tesla - 1st Round

# time complexity: O(N) = N + (M * 3N), where M is the maximum value which is some constant
# and n is the length of the land array
# space complexity: O(1)
from typing import List


def fill_lava(land: List[int]) -> int:
    result = 0
    max_left, max_right = [0] * len(land), [0] * len(land)
    for i in range(0, len(land)):
        max_left[i] = max(land[:i]) if len(land[:i]) > 0 else 0
        max_right[i] = max(land[i:]) if len(land[i:]) > 0 else 0
    for i in range(len(land)):
        curr_lava = min(max_left[i], max_right[i]) - land[i]
        if curr_lava > 0:
            result += curr_lava
    return result
