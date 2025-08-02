from pronounciation_glossary import pronounciation_glossary
import pytest


@pytest.mark.parametrize("words, glossary, expected", [
    (
        "I think artificial intelligence is really cool",
        [("artificial intelligence", "AI"), ("really", "reely")],
        "I think <pron=\"AI\">artificial intelligence</pron> is <pron=\"reely\">really</pron> cool"
    ),
    (
        "I think artificial intelligence is really cool",
        [("artificial intelligence is cool", "AI"), ("really", "reely")],
        "I think artificial intelligence is <pron=\"reely\">really</pron> cool"
    ),
])
def test_pronounciation_glossary(words, glossary, expected):
    assert pronounciation_glossary(words, glossary) == expected
