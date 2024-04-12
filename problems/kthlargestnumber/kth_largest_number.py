from heapq import heapify, heappop, heappush

class Solution:
	# max heap approach: O(Nlog(N))
	def kth_largest(self, arr, k):
		heap = []
		heapify(heap)
		for num in arr: # O(N)
			heappush(heap, -num)
		for i in range(k-1): # O(k)
			heappop(heap)
		return -heappop(heap)
	
if __name__ == '__main__':
	s = Solution()
	tests = [
		([3, 2, 1, 5, 6, 4], 2), # 5
		([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), # 4
	]
	for test in tests:
		print(s.kth_largest(test[0], test[1]))