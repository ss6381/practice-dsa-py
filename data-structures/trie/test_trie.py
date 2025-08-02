from trie import Trie, TrieNode
import pytest


@pytest.fixture
def trie():
    return Trie(TrieNode())


@pytest.mark.parametrize(
    "vocabulary, search",
    [
        (["cat", "cog", "dog", "dash", "do", "cater"], ("wizard", False)),
        (["cat", "cog", "dog", "dash", "do", "cater"], ("dash", True)),
    ],
)
def test_trie(trie: Trie, vocabulary, search):
    for word in vocabulary:
        trie.insert(word)
    assert trie.search(search[0]) == search[1]
