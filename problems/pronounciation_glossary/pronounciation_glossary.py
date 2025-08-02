# Heygen phone screen.

def pronounciation_glossary(words: list[str], glossary: list[(str, str)]) -> list[str]:
    # split words into a list of words
    text_split = words.split(" ")
    matches = []

    # iterate through the glossary.
    for phrase, _ in glossary:
        gloss_split = phrase.split(" ")
        is_match = True
        # iterate through the text split.
        for i in range(len(text_split)):
            if text_split[i] != gloss_split[i]:
                is_match = False
                break
        if is_match:
            matches.append(phrase)

    i = 0
    result = []
    while i < len(text_split):
        result.append(text_split[i])
        for match_phrase in matches:  # ["artificial intelligence is cool"]
            # ["artificial", "intelligence", "is", "cool"]
            match_split = match_phrase.split(' ')
            if text_split[i] == match_split[0]:
                result.append("<pron=\"{}\">{match_phrase}</pron>")
                i += len(match_split)

    return " ".join(result)
