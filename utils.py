#!/bin/env python3
# TODO
from functools import reduce

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import Set, List


class Incrementer:
    """Calling this function returns a number incremented by one per call.

    First returned number is 1, so the returned number is how many this
    instance has been already called."""

    def __init__(self):
        self.state: int = 0

    def __call__(self) -> int:
        self.state += 1
        return self.state


def top_n_indexes(data: list, n: int = None, reverse: bool = True) -> set:
    """Return set of n indexes with highest values in the list.
    :param data: list
    :param n: top n values
    :param reverse: if True (default) n hightest, n lowest otherwise
    """
    # sort by the number
    sort_list: list \
        = sorted(enumerate(data), key=lambda k: k[1], reverse=reverse)

    top: list = sort_list if n is None else sort_list[:n]
    return set(map(lambda a: a[0], top))


if __name__ == '__main__':
    assert (top_n_indexes([1, 8, 6, 4, 5], 3) == {1, 2, 4})
