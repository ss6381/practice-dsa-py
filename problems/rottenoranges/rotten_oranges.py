"""
Argo AI - 1st round
Duo - 1st round

// Given a grid of oranges (fresh, rotten, or none)
// A fresh orange becomes rotten if it is neighboring a rotten orange, in the four grid directions
// RETURN the number of "minutes" before all the fresh oranges are rotten
// otherwise return -1 if there will always be some number of fresh oranges remaining in the grid
"""

from enum import Enum
from typing import List, Tuple, Set
from collections import deque


class OrangeState(Enum):
    NONE = 0
    FRESH = 1
    ROTTEN = 2


def rotten_oranges(grid: List[List[int]]):
    nodes = get_all_rotten(grid)
    mins = bfs(grid, nodes)
    if has_fresh_oranges(grid):
        return -1
    return mins


def get_all_rotten(grid: List[List[int]]) -> List[Tuple[int, int]]:
    result = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == OrangeState.ROTTEN.value:
                result.append((i, j))
    return result


def bfs(grid: List[List[int]], nodes: List[Tuple[int, int]]) -> int:
    visit = set()
    minutes = 0
    q = deque(nodes)
    while q:
        rot = False
        for _ in range(len(q)):
            curr = q.popleft()
            if curr not in visit:
                visit.add(curr)
                neighbors = rot_neighbors(grid=grid, visit=visit, pos=curr)
                if len(neighbors) > 0:
                    rot = True
                for neighbor in neighbors:
                    q.append(neighbor)
        if rot:
            minutes += 1
    return minutes


def rot_neighbors(
    grid: List[List[int]], visit: Set[int], pos: Tuple[int, int]
) -> List[Tuple]:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = []
    for dr, dc in directions:
        row, col = pos[0] + dr, pos[1] + dc
        if (
            row in range(0, len(grid))
            and col in range(0, len(grid[0]))
            and grid[row][col] == OrangeState.FRESH.value
            and (row, col) not in visit
        ):
            grid[row][col] = OrangeState.ROTTEN.value
            result.append((row, col))
    return result


def has_fresh_oranges(grid: List[List[int]]) -> bool:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == OrangeState.FRESH.value:
                return True
    return False
