"""
We have a neardup pipeline at Pinterest, which produces a mapping from every image
to a list of up to k near-duplicate images, such as:
near_dups = {
    "A": ["B", "I", "K"],
    "B": ["A", "D"],
    "C": ["E"],
    "D": [],
    "E": [],
    "F": [],
    "G": ["K"],
    "I": [],
    "K": [],
}
Given a mapping such as this one, form neardup clusters: collections of almost identical images.
In the example above, we would form the following groups: (A, B, D, I, G, K), (C, E), and (F).**
"""
