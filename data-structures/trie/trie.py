from typing import List

num_alpha = 26


class TrieNode:
    def __init__(self):
        self.is_leaf: bool = False
        self.children: List[TrieNode] = [None] * num_alpha


class Trie:

    def __init__(self, root: TrieNode):
        self.root = root

    def insert(self, w: str):
        curr: TrieNode = self.root
        for character in w:
            char_index = ord(character) - ord("a")
            if curr.children[char_index] is None:
                curr.children[char_index] = TrieNode()
            curr = curr.children[char_index]
        curr.is_leaf = True

    def search(self, s: str) -> bool:
        curr: TrieNode = self.root
        for character in s:
            char_index = ord(character) - ord("a")
            if curr.children[char_index] is None:
                return False
            curr = curr.children[char_index]
        return curr.is_leaf
