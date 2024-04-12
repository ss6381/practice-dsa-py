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

from heapq import heapify, heappop, heappush

class Solution:
    
	# time complexity: O(Nlog(N))
	# space complexity: O(N)
	def min_meeting_rooms(self, intervals):
		if not intervals:
			return 0
		intervals.sort(key=lambda x: x[0])
		heap = []
		heapify(heap)
		heappush(heap, intervals[0][1])
		for i in range(1, len(intervals)):
			curr_start = intervals[i][0]
			curr_end = intervals[i][1]
			prev_end = heap[0]
			if curr_start >= prev_end:
				heappop(heap)
			heappush(heap, curr_end)
		return len(heap)
	
if __name__ == '__main__':
	s = Solution()
	tests = [
		[[0, 30],[5, 10],[15, 20]], # 2
		[[7,10],[2,4]], # 1
		[[0, 5],[5, 30],[4, 8]], # 2
	]
	for test in tests:
		print(s.min_meeting_rooms(test))