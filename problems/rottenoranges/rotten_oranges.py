"""
Argo AI - 1st round
Duo - 1st round

// Given a grid of oranges (fresh, rotten, or none)
// A fresh orange becomes rotten if it is neighboring a rotten orange, in the four grid directions
// RETURN the number of "minutes" before all the fresh oranges are rotten
// otherwise return -1 if there will always be some number of fresh oranges remaining in the grid
"""

from enum import Enum

class OrangeState(Enum):
	FRESH = 0
	ROTTEN = 1
	NONE = 2

class Solution:

	def __init__(self, grid):
		self.grid = grid
		self.minutes = 0
		self.fresh = 0

	def rotten_oranges(self):
		self.fresh = self.count_fresh_oranges()
		if self.fresh == 0:
			return 0

		while self.fresh > 0:
			self.rotten_neighbors()
			self.minutes += 1

		return self.minutes
	
	def count_fresh_oranges(self):
		count = 0
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if self.grid[i][j] == OrangeState.FRESH.value:
					count += 1
		return count
	
	def rotten_neighbors(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if self.grid[i][j] == OrangeState.ROTTEN.value:
					if i > 0 and self.grid[i-1][j] == OrangeState.FRESH.value:
						self.grid[i-1][j] = OrangeState.ROTTEN.value
						self.fresh -= 1
					if i < len(self.grid) - 1 and self.grid[i+1][j] == OrangeState.FRESH.value:
						self.grid[i+1][j] = OrangeState.ROTTEN.value
						self.fresh -= 1
					if j > 0 and self.grid[i][j-1] == OrangeState.FRESH.value:
						self.grid[i][j-1] = OrangeState.ROTTEN.value
						self.fresh -= 1
					if j < len(self.grid[i]) - 1 and self.grid[i][j+1] == OrangeState.FRESH.value:
						self.grid[i][j+1] = OrangeState.ROTTEN.value
						self.fresh -= 1

if __name__ == '__main__':
	tests = [
		[[0, 1, 2], [0, 1, 2], [0, 1, 2]],
		[[2, 1, 1],[1, 1, 0],[0, 0, 1]],
	]
	for grid in tests:
		s = Solution(grid)
		print(s.rotten_oranges())
