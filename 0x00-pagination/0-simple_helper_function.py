#!/usr/bin/env python3
"""A script that returns the start and end index of entries on a page"""
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """
        A function that determines the start and end index of data on
        a page relative to the dataset.
        args: page(int): the page in view.
              page_size(int): the number of entries on the page.
        return: a tuple of the start and end index.
    """
    no_entries = page * page_size
    last_index = no_entries
    first_index = last_index - (page_size - 1)
    return (first_index, last_index)
