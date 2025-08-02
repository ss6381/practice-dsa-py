# Pinterest MLE 2025 first round phone screen.
# world -> europe -> (france), (germany) -> (paris), (munich, berlin)

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Tuple
from collections import deque
import time


@dataclass
class TreeNode:
    data: str
    children: List["TreeNode"] = field(default_factory=list)


@dataclass
class GeoNode:
    name: str
    parent: Optional["GeoNode"] = None
    history: Dict[str, Tuple[bool, float]] = field(default_factory=dict)


class GeographicalAccess:

    def __init__(self, root: TreeNode):
        self.root = root
        self.geo_map = self._process_geo_tree(root)

    def _process_geo_tree(self, node: TreeNode) -> Dict[str, Optional["GeoNode"]]:
        """
        Process the geo tree and return a map of location string to GeoNode in O(n) time.
        """
        result: Dict[str, GeoNode] = {node.data: GeoNode(name=node.data, parent=None)}
        q = deque([node])
        while q:
            curr = q.popleft()
            for child in curr.children:
                result[child.data] = GeoNode(name=child.data, parent=result[curr.data])
                q.append(child)
        return result

    def grant_access(self, advertiser_id: str, location: str) -> None:
        self.geo_map[location].history[advertiser_id] = (True, time.time())

    def revoke_access(self, advertiser_id: str, location: str) -> None:
        self.geo_map[location].history[advertiser_id] = (False, time.time())

    def check_access(self, advertiser_id: str, location: str) -> bool:
        if location not in self.geo_map:
            return False
        curr: GeoNode = self.geo_map[location]
        if advertiser_id not in curr.history:
            return False
        access, latest_update = curr.history[advertiser_id]
        while curr.parent:
            curr: GeoNode = curr.parent
            if (
                advertiser_id in curr.history
                and curr.history[advertiser_id][1] > latest_update
            ):
                access = curr.history[advertiser_id][0]
                latest_update = curr.history[advertiser_id][1]
        return access
