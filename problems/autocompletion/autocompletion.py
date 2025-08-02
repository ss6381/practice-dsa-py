# Cartesia first round.
from dataclasses import dataclass

# A
# Node: A -> [Abraham Lincoln, ]

# Ac
# Node: A -> c [Ac]
# Node: A -> b [Ab]


@dataclass
class Node:
    character: str
    children: list


class Autocomplete:

    def __init__(self, vocabulary):
        # Trie
        self.vocabulary = self.process_trie(vocabulary)

    def process_trie(self, vocabulary):
        trie = []
        for vocab in vocabulary:
            curr = Node(vocab[0], [])
            for char in vocab:
                curr.children.append(Node(char, []))
            trie.append(curr)
        return trie

    def autocomplete(self, abbreviation) -> []:
        for node in self.vocabulary:
            result = self.autocomplete_helper(abbreviation, 0, node)
        return result

    def autocomplete_helper(self, abbreviation, index, node, result=[]):
        if abbreviation[index] != node.character:
            return result

        if index >= len(abbreviation):
            return result

        for char_node in node.children:
            return self.autocomplete_helper(abbreviation[index+1], char_node)

        return result

# len(names): n
# len(name): l
# len(abbreviation): k

# time: O(l*n)
# space: O(l*n)


def test1():
    print("--- TEST 1 ---")
    abbrev = "Abr"
    names = [
        "Sparsh",
        "Abraham Lincoln",
        "Abraham Conway",
        "Brandon",
        "Abriel Dare"
    ]
    autocomplete = Autocomplete(names)
    print(autocomplete.autocomplete(abbrev))


test1()
