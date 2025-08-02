"""
Meta - 1st round
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of meeting rooms required.

*Example 1:Input:* [[0, 30],[5, 10],[15, 20]]*Output:* 2
*Example 2:Input:* [[7,10],[2,4]] *Output:* 1

*Example 3:Input:* [[0, 5],[5, 30],[4, 8]]
[[0, 5],[4, 8],[5, 30]]

-------------------
    ---
	    ---
"""

from heapq import heappop, heappush
from typing import List, Tuple


# time complexity: O(Nlog(N))
# space complexity: O(N)
def min_meeting_rooms(intervals: List[Tuple[int, int]]) -> int:
    """
    Find the minimum number of meeting rooms required.

    We use a min heap to keep track of the end times of the meetings.
    We sort the intervals by start time.
    For each interval, we check if the start time is greater than the end time of the
    previous meeting. If it is, we pop the end time from the heap.
    We push the end time of the current meeting onto the heap.
    The size of the heap at the end is the minimum number of meeting rooms required.

    Args:
        intervals: List[List[int]] - List of meeting intervals.

    Returns:
        int: The minimum number of meeting rooms required.
    """
    intervals.sort(key=lambda x: x[0])  # O(NlogN)
    heap = [intervals[0][1]]
    for start, end in intervals[1:]:  # O(N)
        if start >= heap[0]:
            heappop(heap)  # O(logN)
        heappush(heap, end)  # O(logN)
    return len(heap)


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Qs:
    - Is the intervals list provided to us pre-sorted?
    - Can an interval start time be < 0?
    - Do we have a guarantee that the end time provided will be greater than start time?
    Approach:
    - We can sort the intervals by start time O(nlogn) time, using Timsort
    - We iterate through the intervals, and if we see that an interval starts before the previous
        interval has ended, we will merge those intervals.
    Edge case:
    - [[1, 4], [5, 7], [4, 7]]: We will merge the intervals in-place so that we can merge multiple overlapping intervals.
    Tradeoffs:
    - If we don't sort, we would have to compare every interval with every other interval O(n^2)
    - What sorting algorithms should we use? Tim sort vs. merge O(nlogn) / quick O(nlogn) / insertion O(n^2) / selection O(n^2)
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])  # O(nlogn): using TimSort vs. other sort
    result: List[List[int]] = [intervals[0]]
    for start, end in intervals[1:]:
        prev_end = result[-1][1]
        if start <= prev_end:
            result[-1][1] = max(prev_end, end)
        else:
            result.append([start, end])
    return result


def merge_k_interval_lists(
    intervals: List[List[Tuple[int, int]]]
) -> List[Tuple[int, int]]:
    """
    Merge k sorted interval lists into one sorted interval list and merge any overlapping intervals.
    Questions:
    - Are any of the lists sorted or ordered? Assume yes.
    Approach:
    - If the lists are not ordered, we can combine all the lists into one list, sort it,
        and then iterate through the intervals, comparing the start of the curr interval
        against the end of the previous interval and merging them if they overlap.
        This solution will be dominated by the time complexity of the sort, since that is O(nlogn),
        and the other work will only be O(n) in the worst case.
    - If the lists are sorted, then we can use an approach similar to the merge lists algorithm
        that merge sort uses O(n), where we use two pointers to iterate through the lists while
        the both pointers are less than their respective array lengths, pushing the lower value into
        the result and incrementing that pointer. Then we can iterate through the intervals similar to
        the previous approach.
        - Consideration: We can use a priority queue like a min heap to keep track of the end of the
            interval while iterating through the intervals, where we will only need to check each of
            the interval lists which will be O(k).
    """
    pass

    # result = [combined_intervals[0]]
    # for start, end in combined_intervals[1:]:
    #     prev_end = result[-1][1]
    #     if start <= prev_end:
    #         result[-1][1] = max(end, prev_end)
    #     else:
    #         result.append((start, end))

    #     # add
    # return result
