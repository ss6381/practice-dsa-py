# # find all contiguous permutations of b in s
# def SlidingWindow(b: str, s: str) -> list[list[int]]:
#     permutations = []
#     bMap = createComparisonMap(b)  # O(b)
#     for i in range(len(s)):  # O(s * b)
#         if s[i] in bMap:
#             for k in range(len(b)):
#                 if s[i + k] == b[k]:
#                     permutations.append([i, i + k])
#     return permutations

from typing import List, Tuple
from collections import Counter


def sliding_window(cipher: str, input: str) -> List[Tuple[int, int]]:
    cipher_count = Counter(cipher)
    result = []
    for i in range(len(input)):
        if input[i] in cipher_count.keys():
            if i + len(cipher) - 1 >= len(input):
                return result
            window = str(input[i : i + len(cipher)])
            if Counter(window) == cipher_count:
                result.append((i, i + len(cipher) - 1))
    return result
