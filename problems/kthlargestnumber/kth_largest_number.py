from heapq import heapify, heappop
from typing import List


# max heap approach: O(n)
def kth_largest(arr: List[int], k: int) -> int:
    heap: List[int] = [-x for x in arr]
    heapify(heap)  # O(N)
    for _ in range(k - 1):  # O(k)
        heappop(heap)
    return -heappop(heap)
