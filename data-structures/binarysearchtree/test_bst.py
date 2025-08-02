from bst import BinarySearchTree, Node
import pytest


@pytest.fixture
def tree():
    node = Node(100)
    return BinarySearchTree(root=node)


def test_node(tree: BinarySearchTree):
    node = tree.root
    input = 5
    for k in range(input + 1):
        node.insert(k)
        assert node.search(k) == Node(k)

    assert node.search(25) != Node(25)

    # TODO: Implement remove method for node
    # assert node.remove(25) == False
    # assert node.search(4) == True
    # assert node.remove(4) == True
    # assert node.search(4) == False


def test_binary_search_tree(tree: BinarySearchTree):
    input = 5
    for k in range(input + 1):
        tree.insert(k)
        assert tree.search(k) == Node(k)

    assert tree.search(25) != Node(25)

    # TODO: Implement remove method for binary search tree
    # assert tree.remove(25) == False
    # assert tree.search(4) == True
    # assert tree.remove(4) == True
    # assert tree.search(4) == False
